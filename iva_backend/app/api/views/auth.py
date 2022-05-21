from datetime import timedelta

from django.conf import settings
from django.core.exceptions import BadRequest
from django.utils import timezone
from oauth2_provider.models import RefreshToken, AccessToken, Application
from oauthlib.common import generate_token
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.auth import UserRegistrationSerializer
from iva_backend.app.models import CustomUser


class RegisterUserAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        access_token, refresh_token = self.__generate_auth_tokens(user)
        return Response(
            data={
                'access_token': access_token.token,
                'refresh_token': refresh_token.token
            },
            status=status.HTTP_201_CREATED
        )

    def __generate_auth_tokens(self, user: CustomUser):
        expire_in = settings.OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
        try:
            app = Application.objects.get(name=settings.OAUTH2_APP_NAME)
        except Application.DoesNotExist:
            raise BadRequest('OAuth2 App missing')
        else:
            access_token = AccessToken.objects.create(
                user=user,
                application=app,
                expires=timezone.now() + timedelta(seconds=expire_in),
                token=generate_token()
            )

            refresh_token = RefreshToken.objects.create(
                user=user,
                application=app,
                access_token=access_token,
                token=generate_token()
            )

            return access_token, refresh_token
