from django.urls import path
from .views import UserListView, UserDetailView, BanUserView

urlpatterns = [

    path('users/', UserListView.as_view(), name='user-list'),


    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),


    path('ban-user/<int:pk>/', BanUserView.as_view(), name='ban_user'),
]