from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='info-index'),
    path(f'family/<int:id>', views.family, name='info-family'),
    path('animal/<int:id>', views.animal, name='info-animal'),
]