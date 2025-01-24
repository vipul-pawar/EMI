from django.urls import path, include
from  . import views
urlpatterns = [
    path('', views.emi_calculator_view, name='calculator'),
    path('result', views.result, name='result'),
    path('base', views.base, name='base'),
]
