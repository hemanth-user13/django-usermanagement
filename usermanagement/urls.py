from django.urls import path
from .views import RegisterView, LoginView, SuperAdminLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('superadmin-login/', SuperAdminLoginView.as_view(), name='superadmin-login'),
]
