from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('fake_users/<int:num>', views.user_factory, name='fake-users'),
    path('add_cards/', views.populate_users_with_cards, name='add-cards'),
]
