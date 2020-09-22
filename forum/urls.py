from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from articles.views import UserViewSet, GroupViewSet

# configure users and groups routers (from articles app)
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)), # users and groups urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # login urls
    path('articles/', include('articles.urls')), # articles urls
    path('admin/', admin.site.urls),
]


