from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegistrationAPIView, UserUpdateAPIView

urlpatterns = [
    path('signup/', RegistrationAPIView.as_view()),
    path('signin/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('update/<int:user_pk>/', UserUpdateAPIView.as_view())
]
