
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path("AddProductDetails",views.AddProductDetails,name="AddProductDetails"),
    path("ShowProducts",views.ShowProducts,name="ShowProducts"),
    path("EditPage/<int:pk>",views.EditPage,name="EditPage"),
    path("EditProductDetails/<int:pk>",views.EditProductDetails,name="EditProductDetails"),
    path("DeleteItems/<int:pk>",views.DeleteItem,name="DeleteItem")
]