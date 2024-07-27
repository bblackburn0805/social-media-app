from django.urls import path
from . import views
from .views import AccountView

urlpatterns = [
    path('account', views.AccountView.as_view(), name='account'),
]
