from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Sum
from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductListFilter
from .forms import UserUpdateForm
from .models import Product, DetailImage, Order, OrderItem, Worker, OurService, Link
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def index(request):
    all_products = Product.objects.all()
    social_links = Link.objects.filter(is_active=True)

    context = {
        'trending_now': all_products,
        'always_popular': all_products,
        'social_links': social_links,
    }

    return render(request, template_name='buyershop/index.html', context=context)


def about_us(request):
    workers = Worker.objects.all()
    our_services = OurService.objects.all()
    social_links = Link.objects.filter(is_active=True)

    context = {
        'workers': workers,
        'our_services': our_services,
        'social_links': social_links,
    }
    return render(request, template_name='buyershop/about.html', context=context)


def add_to_cart(request, product_pk):

    try:
        order = Order.objects.get(user=request.user, status='До ожидании')
    except ObjectDoesNotExist:
        # Create a new order if it doesn't exist
        order = Order.objects.create(user=request.user, status='До ожидании')
    order_items = order.orderitems.all()
    product_ids = order_items.values_list('product_id', flat=True)
    if product_pk not in product_ids:
        OrderItem(order=order, product_id=product_pk).save()
    else:
        order_item = order_items.get(product_id=product_pk)
        order_item.quantity += 1
        order_item.save()

    return redirect('product_list')


class OrderItemsListView(ListView):
    template_name = 'buyershop/product-order.html'
    queryset = OrderItem.objects.filter(order__status='До ожидании').annotate(
        total_price=F('product__price') * F('quantity')
    )
    context_object_name = 'order_items'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        qs = qs.filter(order__user=user)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['grant_total'] = context['order_items'].aggregate(grand_total=Sum('total_price'))['grand_total']
        return context

    def post(self, request):
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        for order_item_pk, quantity in data.items():
            order_item = OrderItem.objects.get(pk=order_item_pk)
            order_item.quantity = quantity[0]
            order_item.save()

        order = order_item.order
        order.status = 'В ожидании'
        order.save()

        return super(OrderItemsListView, self).get(request)


class FilteredListView(ListView):
    filterset_class = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filterset = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class ProductList(FilteredListView):
    model = Product
    filterset_class = ProductListFilter
    template_name = 'buyershop/product-list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_order_by(self):
        order_by = self.request.GET.get('order_by')
        if order_by == 'oldest':
            return 'created_date'
        elif order_by == 'newest':
            return '-created_date'
        elif order_by == 'low_price':
            return '-price'
        elif order_by == 'high_price':
            return 'price'
        elif order_by == 'abc':
            return 'name'
        else:
            return '-id'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        order_by = self.get_order_by()
        filterset = self.filterset_class(self.request.GET, queryset=queryset)
        filtered_queryset = filterset.qs.order_by(order_by)
        return filtered_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_by'] = self.get_order_by()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'buyershop/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['detail_images'] = DetailImage.objects.filter(product=product)
        return context

    def post(self, request, slug):

        try:
            order = Order.objects.get(user=request.user, status='До ожидании')
        except ObjectDoesNotExist:
            # Create a new order if it doesn't exist
            order = Order.objects.create(user=request.user, status='До ожидании')

        order_items = order.orderitems.all()
        product_ids = order_items.values_list('product_id', flat=True)

        product = Product.objects.get(slug=slug)
        quantity = int(request.POST['quantity'])

        if product.pk not in product_ids:
            OrderItem(order=order, product=product, quantity=quantity).save()
        else:
            order_item = order_items.get(product_id=product)
            order_item.quantity += quantity
            order_item.save()

        return redirect('product_list')


def personal_area(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('personal_area')
        messages.error(request,
                       'Повторите попытку, убедитесь что поля заполнены в правильном формате или данные с таким '
                       'пользователем уже существует!')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, template_name='buyershop/personal_area.html', context={'user': user, 'form': form})


