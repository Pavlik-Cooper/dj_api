from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from .serializers import EntityModelSerializer
from entities.models import Entity
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from accounts.api.permissions import IsOwnerOrReadOnly


class EntityListCreateView(generics.ListCreateAPIView):
    serializer_class = EntityModelSerializer
    search_fields = ('user__username', 'content', 'title', 'user__email')
    ordering_fields = ('id', 'title', 'user__username', 'created_at')

    def get_queryset(self):
        qs = Entity.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EntityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = EntityModelSerializer
    lookup_field = 'id'
    queryset = Entity.objects.all()

    # def get(self, request, *args, **kwargs):
    #     passed_id = request.GET.get('id')
    #     if not passed_id is None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request,*args,**kwargs)

    # def get_object(self,*args,**kwargs):
    #     return get_object_or_404(Entity,id=self.kwargs.get('id'))

