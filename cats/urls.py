from django.urls import path

from cats import views

app_name = 'cats'

urlpatterns = [
    path('', views.CatList.as_view(), name='cat_list'),
    path('breed_list/', views.BreedList.as_view(), name='breed_list'),
    path('breed_create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breed_update/<int:pk>/', views.BreedUpdate.as_view(), name='breed_update'),
    path('breed_delete/<int:pk>/', views.BreedDelete.as_view(), name='breed_delete'),
    path('cat_create/', views.CatCreate.as_view(), name='cat_create'),
    path('cat_update/<int:pk>/', views.CatUpdate.as_view(), name='cat_update'),
    path('cat_delete/<int:pk>/', views.CatDelete.as_view(), name='cat_delete'),
]
