from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category>/', views.index, name='category_filter'),
]
