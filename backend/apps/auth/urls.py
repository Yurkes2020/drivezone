from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import BuyerRegisterView, SellerRegisterView, ManagerRegisterView

urlpatterns = [

    path('register/buyer/', BuyerRegisterView.as_view(), name='buyer-register'),


    path('register/seller/', SellerRegisterView.as_view(), name='seller-register'),


    path('register/manager/', ManagerRegisterView.as_view(), name='manager-register'),


    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]