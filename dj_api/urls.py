from django.contrib import admin
from django.urls import path,re_path

# from entities.views import EntityList,EntityDetail
from entities.api.views import *
from accounts.api.views import RegisterAPIView
from accounts.api.user.views import UserDetailView,UserEntityListView
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/auth/', obtain_jwt_token),
    path('api/auth/refresh/', refresh_jwt_token),
    path('api/auth/register/',RegisterAPIView.as_view()),
    path('api/users/<int:id>/', UserDetailView.as_view(),name='user.detail'),
    path('api/users/<int:id>/entities/', UserEntityListView.as_view()),

    path('api/entities/', EntityListCreateView.as_view()),
    # path('api/entities/create/', EntityListCreateView.as_view()),
    path('api/entities/<int:id>/',EntityDetailView.as_view(),name='entity.detail'),
    # path('api/entities/<int:id>/update', EntityDetailView.as_view()),
    # path('api/entities/<int:id>/delete', EntityDetailView.as_view()),
]
