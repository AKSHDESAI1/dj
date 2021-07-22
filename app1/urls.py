from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="ShopHome"),
    path('blogpost/<int:id1>', views.blogpost, name="BlogHome")


]