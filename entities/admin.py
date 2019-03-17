from django.contrib import admin

# Register your models here.
from .models import Entity
from .forms import EntityModelForm


class EntityAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','content']
    form = EntityModelForm

    # class Meta:
    #     model = Entity

admin.site.register(Entity,EntityAdmin)