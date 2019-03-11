from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.index, name = 'index'), # /boards
    # path('new/', views.new),
    path('new/', views.new, name = 'new'),
    # path('create/', views.create),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
]
