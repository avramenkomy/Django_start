from common.views import index, RegisterView, CreateUserProfile
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import login, logout
from django.urls import reverse_lazy

app_name = 'common'
urlpatterns = [
    path('', index, name='index'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]