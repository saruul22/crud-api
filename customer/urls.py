from django.urls import path
from .views import CustomerAPIView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', CustomerAPIView.as_view(), name='customer-list'),
    path('<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),
]