
This repo does not comleted yet

## Forum API:  
  
## Installed Applications:  

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
    'articles.apps.ArticlesConfig',
    'posts.apps.PostesConfig',
]
```

### Features:  
    includin login + logout urls from rest_framework.urls

    - posts app :
    Posts crud operations using viewsets + adding comments action  
    posts are associated with a creator
    Only authenticated users may create posts
    Only the creator of a posts may update or delete it
    Unauthenticated requests have full read-only access

    - articles app :
    Articles crud operations using generic views  
    articles are associated with a creator
    Only authenticated users may create articles
    Only the creator of a articles may update or delete it
    Unauthenticated requests have full read-only access

    api documentation with drf_yasg



