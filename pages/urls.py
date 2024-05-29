from django.urls import path
from .views import homeview, successview

urlpatterns = [
    path("", homeview, name="home"),
    path("success/", successview, name="success"),
]
