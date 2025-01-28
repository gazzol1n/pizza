from django.urls import path
from .views import CapitalListView

urlpatterns = [
    path('capitals/', CapitalListView.as_view(), name='capital-list'),
]
