from django.urls import path
from .views import get_users


urlpatterns = [
     path('users/', get_users, name='get-users')
     # path('stock/', StockListCreateView.as_view(), name='stock-create'),
]