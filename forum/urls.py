from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usersgroups.urls import router # import user and groups routers


urlpatterns = [
    # login urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # articles urls
    path('articles/', include('articles.urls')), 
    # posts urls
    path('posts/', include('posts.urls')), 
    # admin urls
    path('admin/', admin.site.urls),
]


# appending users and groups urls
urlpatterns += router.urls
