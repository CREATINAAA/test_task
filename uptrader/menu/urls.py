from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='open_menu'),
    path('<slug:slug>/', views.menu, name='draw_menu'),
]