from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import URLField
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import Serializer

from src.petite_url.services.petite_url_service import create_petite_url


class InputBodySerializer(Serializer):
    target_url = URLField(required=True)


@api_view(["POST"])
@permission_classes([AllowAny])
def petitify_url_view(request: Request) -> Response:
    body = InputBodySerializer(data=request.data)
    body.is_valid(raise_exception=True)

    target_url = body.validated_data["target_url"]

    petite_url = create_petite_url(target_url)

    petite_url_view = reverse(
        viewname="petite-url",
        args=[petite_url.petite_code],
        request=request,
    )
    return Response(petite_url_view, status=201)
