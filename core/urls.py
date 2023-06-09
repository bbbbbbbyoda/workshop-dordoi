from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('supersecretadmin/', admin.site.urls),
    path('', include('buyershop.urls')),
    path('account/', include('account.urls')),
    path('textile/', include('textilefactory.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)