from rest_framework import generics, permissions, pagination
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from entities.api.serializers import EntityInlineUserModelSerializer
User = get_user_model()
from entities.models import Entity


class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # permissions.AllowAny
    queryset = User.objects.all().filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = "id"

    def get_serializer_context(self):
        return {'request': self.request}


class UserEntityListView(generics.ListAPIView):
    # pagination_class = Pagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # permissions.AllowAny
    serializer_class = EntityInlineUserModelSerializer
    search_fields = ('title', 'content')
    ordering_fields = ('id', 'title', 'created_at')

    def get_queryset(self,*args,**kwargs):
        id = self.kwargs.get('id')
        if id is None:
            return Entity.objects.none()
        return Entity.objects.filter(user__id=id)
