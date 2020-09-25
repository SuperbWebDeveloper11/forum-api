from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from usersgroups.urls import router as usersgroups_router # import user and groups routers
from posts.urls import router as posts_router # import post routers


# drf_yasg configuration
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# drf_yasg configuration
schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
            ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        )



urlpatterns = [
    # login urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # articles urls
    path('articles/', include('articles.urls')), 
    # admin urls
    path('admin/', admin.site.urls),
    # drf_yasg configuration
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),               
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),                         
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 

]


# appending 'users and groups' urls and 'posts' urls
urlpatterns += usersgroups_router.urls
urlpatterns += posts_router.urls
