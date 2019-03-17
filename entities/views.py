from django.http import JsonResponse,HttpResponse
from django.views.generic import View
# Create your views here.
from .models import Entity


class EntityDetail(View):
    def get(self,request,*args,**kwargs):
        obj = Entity.objects.first()
        return HttpResponse(obj.serialize(),content_type="application/json")

    def put(self,request,*args,**kwargs):
        obj = Entity.objects.first()
        return HttpResponse(obj.serialize(), content_type="application/json")

    def delete(self,request,*args,**kwargs):
        obj = Entity.objects.first()
        return HttpResponse(obj.serialize(), content_type="application/json")


class EntityList(View):
    def get(self,request,*args,**kwargs):
        qs = Entity.objects.all().serialize()
        return HttpResponse(qs,content_type="application/json")

    def post(self,request,*args,**kwargs):
        qs = Entity.objects.create(name=request.title)
        return HttpResponse(qs, content_type="application/json")
