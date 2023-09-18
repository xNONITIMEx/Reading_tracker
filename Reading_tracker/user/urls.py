from django.urls import path
from .views import sign_up, Login

app_name = 'user'
urlpatterns = [
    path('sign_up', sign_up, name='sign up'),
    path('login', Login.as_view(), name='login'),
]
