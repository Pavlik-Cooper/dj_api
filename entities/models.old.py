from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json
from django.shortcuts import reverse

def upload_image(instance,filename):
    return f"images/{instance}/{filename}"


class EntityQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('user','title','content'))
        return json.dumps(list_values)


class EntityManager(models.Manager):
    def get_queryset(self):
        return EntityQuerySet(self.model,using=self._db)


class Entity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return self.title

    objects = EntityManager()

    def __str__(self):
        return self.title

    def serialize(self):
        json_data = serialize('json',[self],fields=('user','title','content'))
        cleaned_json = json.loads(json_data)
        json_data = json.dumps(cleaned_json[0]['fields'])
        return json_data