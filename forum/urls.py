from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usersgroups.urls import router as usersgroups_router # import user and groups routers
from posts.urls import router as posts_router # import post routers


urlpatterns = [
    # login urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # articles urls
    path('articles/', include('articles.urls')), 
    # admin urls
    path('admin/', admin.site.urls),
]


# appending 'users and groups' urls and 'posts' urls
urlpatterns += usersgroups_router.urls
urlpatterns += posts_router.urls
