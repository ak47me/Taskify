from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index,name = "index"),
    path('', views.first,{},name = "first"),
    path("create/",views.create,name = "create"),
    path('view/',views.view,name = 'view'),
    path('base/',views.base,name = 'base'),
    ]
