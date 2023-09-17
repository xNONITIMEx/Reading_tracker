from django.urls import path
from .views import sign_in

app_name = 'user'
urlpatterns = [
    path('sign_in', sign_in, name='sign in')
]