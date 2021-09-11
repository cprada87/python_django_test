from django.urls import path, include

from rest_framework import routers
from .views import UserViewSet, index

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path(r'auth/index', index, name='index'),

]
