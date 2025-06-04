from django.urls import path
from solveit import views


urlpatterns = [
    path('', views.index, name="index"),
]
