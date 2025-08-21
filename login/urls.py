from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('success/', views.success_view, name="success"),
]

