from rest_framework import routers
from . import views
from django.urls import path, include  # Import path and include

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

urlpatterns = [
    # ... other URLs ...
    path('', include(router.urls)),
]
