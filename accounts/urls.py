from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.product,name='products'),
    path('customer/<str:pk>/',views.customer,name='customers'),
    path('createOrder',views.createOrder,name='createOrder'),
    path('UpdateOrder/<str:pk>',views.UpdateOrder,name='UpdateOrder'),
    path('updateCustomer/<str:pk>',views.updateCustomer,name='updateCustomer'),
    path('deleteOrder/<str:pk>',views.deleteOrder,name='deleteOrder'),
    path('createCustomer',views.createCustomer,name='createCustomer'),
]
