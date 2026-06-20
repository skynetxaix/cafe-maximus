from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(), name='index'),
    path('items/',views.items,name='items'),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
    path('add/',views.CreateItem.as_view(), name='add_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item, name='delete_item'),
]
