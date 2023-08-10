from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from src.petite_url.services.petite_url_service import get_petite_url


@api_view(["GET"])
@permission_classes([AllowAny])
def petite_url_view(_request: Request, petite_code: str) -> HttpResponseRedirect:
    petite_url = get_petite_url(petite_code)
    return redirect(petite_url.target_url, permanent=False)
