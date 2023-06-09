from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('authentication/', views.authentication_view, name='authentication'),
    path('logout/', views.logout_view, name='exit'),
]