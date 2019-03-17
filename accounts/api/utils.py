from dj_api.settings import JWT_AUTH
from .serializers import UserPublicSerializer
import datetime
from django.utils import timezone

expire_delta = JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserPublicSerializer(user, context={'request': request}).data,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }
