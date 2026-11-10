from django.urls import path

from .views import comprobar_paridad


urlpatterns = [
    path("", comprobar_paridad, name="comprobar_paridad"),
]