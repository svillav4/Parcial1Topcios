from django.urls import path
from .views import HomePageView, RegisterPageView, ListPageView, StatsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('list/', ListPageView.as_view(), name='list'),
    path('stats/', StatsPageView.as_view(), name='stats'),
]