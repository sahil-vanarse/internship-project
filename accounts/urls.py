from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, signup_view, forgot_password_view, change_password_view, dashboard_view, profile_view, home_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('forgot_password/', forgot_password_view, name='forgot_password'),
    path('change_password/', change_password_view, name='change_password'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    
]
