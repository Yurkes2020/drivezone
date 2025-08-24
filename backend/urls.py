from django.urls import path, include

urlpatterns = [
    path('', include('backend.apps.users.urls')),
    path('', include('backend.apps.cars.urls')),
    path('', include('backend.apps.dealers.urls')),
    path('', include('backend.apps.premium.urls')),
    path('', include('backend.apps.brands.urls')),
    path('', include('backend.apps.auth.urls')),
    path('', include('backend.apps.currency.urls')),
]