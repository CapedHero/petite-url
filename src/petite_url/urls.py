from django.urls import path

from src.petite_url.views import petite_url_view, petitify_url_view

api_urlpatterns = [
    path("petitify", petitify_url_view, name="petitify-url"),
    path("go/<str:petite_code>", petite_url_view, name="petite-url"),
]
