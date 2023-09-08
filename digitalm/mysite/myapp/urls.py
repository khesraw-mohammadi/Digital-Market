from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.index, name="index"),
    path('product/<int:id>/', views.detail, name="detail"),
    path('order_process/<int:id>/', views.order_process, name="order_process"),
    path('create_product/', views.create_product, name="create_product"),
    path('edit_product/<int:id>/', views.edit_product, name="edit_product"),
    path('delete/<int:id>/', views.product_delete, name="delete"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name="logout"),
    path('invalid/', views.invalid, name="invalid"),
    path('purchases/', views.my_purchases, name="purchases"),
    path('sales/', views.sales, name="sales"),


]
