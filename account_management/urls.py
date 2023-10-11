from django.urls import path

from account_management.views import CreateAccount

urlpatterns = [
    path('register', CreateAccount.as_view(), name='register'),
]