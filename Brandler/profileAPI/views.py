from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from profileAPI.models import Account
from .serializers import AccountSerializer


# Create your views here.

class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
