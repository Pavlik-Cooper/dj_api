from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model

from entities.api.serializers import EntityInlineUserModelSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # entities = EntityModelSerializer(read_only=True)

    entities = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'entities'
        ]

    def get_url(self,obj):
        # return f'/api/users/{obj.id}/'
        return api_reverse('user.detail',kwargs={'id':obj.id},request=self.context['request'])

    def get_recent_entities(self,obj):
        limit = 5
        request = self.context.get('request')
        if request:
            limit_p = request.GET.get('limit')
            try:
                limit = int(limit_p)
            except:
                pass

        qs = obj.entity_set.order_by("-created_at")[:limit]
        return EntityInlineUserModelSerializer(qs, many=True, context=self.context).data

    def get_entities(self,obj):
        return {
            'url': self.get_url(obj) + 'entities/',
            'recent': self.get_recent_entities(obj)
        }
