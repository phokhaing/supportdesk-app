from rest_framework.routers import DefaultRouter
from .views import UserManagement
from rest_framework import viewsets

router = DefaultRouter()
router.register('', viewset=UserManagement, basename='users')
urlpatterns = router.urls