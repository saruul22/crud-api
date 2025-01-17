from django.urls import path
from .views import CustomerAPIView, LoginView, LogoutView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', CustomerAPIView.as_view(), name='customer-list'),
    path('<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]