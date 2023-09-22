from django.urls import path
from .views import sign_up, Login, Logout, activate

app_name = 'user'
urlpatterns = [
    path('sign_up', sign_up, name='sign up'),
    path('login', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', activate, name='activate')
]
