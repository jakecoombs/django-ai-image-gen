from django.urls import path

from . import views

app_name = "gen"
urlpatterns = [
    path("", views.generate_image, name="generate_image"),
]
