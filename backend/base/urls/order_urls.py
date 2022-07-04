from django.urls import path
from base.views import order_views as views


urlpatterns = [
    path('add/',views.addOrderItems,name='orders-add'),
    path('my/',views.getMyOrders,name='user-orders'),
    path('<str:pk>/',views.getOrderById,name='user-order')
]
