from django.urls import path
from.import views

urlpatterns = [
path('', views.saludo),
path('saludo/<str:nombre>/', views.saludar_usuario),
path('edad/<int:edad>/', views.edad),
path('inicio/1/', views.inicio, name='inicio'),
]
