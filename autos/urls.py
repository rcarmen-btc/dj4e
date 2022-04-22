from django.urls import path

from . import views

app_name = 'autos'

urlpatterns = [
        path('', views.AutosList.as_view(), name='autos_list'),
        path('makes_list/', views.MakesList.as_view(), name='makes_list'),
        path('makes_list/makes_update/<int:pk>', views.MakesUpdate.as_view(), name='makes_update'),
        path('makes_list/makes_delete/<int:pk>', views.MakesDelete.as_view(), name='makes_delete'),
        path('makes_list/makes_create/', views.MakesCreate.as_view(), name='makes_create'),
        path('autos_update/<int:pk>', views.AutoUpdate.as_view(), name='autos_update'),
        path('autos_delete/<int:pk>', views.AutoDelete.as_view(), name='autos_delete'),
        path('auto_create/', views.AutoCreate.as_view(), name='autos_create'),
        

]
