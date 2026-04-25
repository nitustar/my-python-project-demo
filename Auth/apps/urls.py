from django.urls import path
from .views import RegisterView, LoginView, health_check

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('health/', health_check),
]
