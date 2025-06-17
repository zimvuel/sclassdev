from .views import view
from django.urls import path

urlpatterns = [
    path('', view, name='app_landing'),
]