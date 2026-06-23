from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(), name='index'),
    path('items/',views.items,name='items'),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
    path('add/',views.CreateItem.as_view(), name='add_item'),
    path('update/<int:pk>/',views.UpdateItem.as_view(),name='update_item'),
    path('delete/<int:pk>/',views.DeleteItem.as_view(), name='delete_item'),
    path('order/<int:pk>/',views.Order_item,name='Order_item' ),
    path('orders/',views.Order_list.as_view(),name='Orders'),
    path('delete_order/<int:pk>/',views.delete_order,name='delete_order')
]
