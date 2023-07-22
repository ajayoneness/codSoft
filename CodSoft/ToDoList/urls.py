from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('todolist/',views.todolist, name="todolist"),
    path('delete/<int:id>/', views.deleteItem, name='delete_item'),
    path('update/<int:id>/', views.updateItem, name='update_item'),
]
