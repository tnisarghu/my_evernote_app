from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'search', views.SearchIndexViewSet)

urlpatterns = [
    # ... other URLs ...
    path('', include(router.urls)),
]
