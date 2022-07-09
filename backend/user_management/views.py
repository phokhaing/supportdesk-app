from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoObjectPermissions

from .serializer import UserDetailsSerializer
from .models import User


class UserManagement(viewsets.ModelViewSet):
	# authentication_classes = [TokenAuthentication]
	# permission_classes = [DjangoObjectPermissions]
	queryset = User.objects.all()
	serializer_class = UserDetailsSerializer
