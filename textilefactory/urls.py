from django.urls import path

from . import views
urlpatterns = [
    path('textile/', views.textile_order, name='textile')
]
