from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.getNotes),
    path('note/<str:pk>/', views.getNote),
    path('create-note/', views.createNote),
    path('delete-note/<str:pk>/', views.deleteNote),
    path('update-note/<str:pk>/', views.updateNote),
]