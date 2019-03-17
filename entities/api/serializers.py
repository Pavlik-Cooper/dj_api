from rest_framework import serializers
from entities.models import Entity
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse


class EntityInlineUserModelSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Entity
        fields = [
            'id',
            'title',
            'content',
            'image',
            'created_at',
            'url'
        ]

    def get_url(self,obj):
        # return f"/api/entities/{obj.id}/"
        return api_reverse('entity.detail',kwargs={'id':obj.id},request=self.context['request'])


class EntityModelSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Entity
        fields = [
            'id',
            'user',
            'title',
            'content',
            'image',
            'created_at',
            'url'
        ]
        read_only_fields = ['user']

    # def get_user(self,obj):
    #     return {
    #         'id':obj.user.id,
    #         'username':obj.user.username
    #     }
    #

    def get_url(self,obj):
        # return f"/api/entities/{obj.id}/"
        return api_reverse('entity.detail', kwargs={'id': obj.id}, request=self.context['request'])

    def validate(self, attrs):
        content = attrs.get('content')
        image = attrs.get('image')

        if content == "":
            content = None
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")
        return super().validate(attrs)
