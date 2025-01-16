from django.urls import path
from .views import CustomerAPIView

urlpatterns = [
    # API endpoints using CustomerAPIView
    path('', CustomerAPIView.as_view(), name='customer-list'),
    path('<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),
]