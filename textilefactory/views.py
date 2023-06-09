from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import TextileOrderForm, TextileOrderFile
from .models import TextileOrder


def textile_order(request):
    user = request.user
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('register')

        form = TextileOrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user

            for f in request.FILES.getlist('files', None):
                # проверяем, существует ли файл уже в базе данных
                file_instance = TextileOrderFile.objects.create(files=f)

            obj.files = file_instance
            obj.save()
            return redirect('index')
    form = TextileOrderForm()
    return render(request, template_name='textile.html', context={'form': form})