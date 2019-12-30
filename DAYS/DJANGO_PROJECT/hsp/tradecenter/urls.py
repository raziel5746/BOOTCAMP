from django.urls import path
from . import views

urlpatterns = [
    path('populator/', views.populator, name='populator')
]