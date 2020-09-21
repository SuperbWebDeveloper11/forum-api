
This repo does not comleted yet

## Forum API:  
  

### Features:  
    Post crud operations  
    Comment crud operations  
    users could like post    
    users could like comments    
    users could signup + login (not finished yet)
    access control with token
    api documentation with drf_yasg

  
### Models:   
    Post,   
    Comment,   
    LikePost,   
    LikeComments  
  
### Serializers:  
    PostSerializer   
    CommentSerializer   
    LikePostSerializer   
    LikeCommentSerializer  
  
  
### Ex: requesting the first post   
  
curl localhost:8000/blog/1/ | json_pp   
  
```json
{  
    "id" : 1,  
    "body" : "first post",  
    "created_by" : 1,  
    "likes" : [  
    {  
        "post" : 1,  
        "liked_by" : 2,  
        "id" : 1  
    }  
    ],  
    "comments" : [  
    {  
        "post" : 1,  
        "id" : 1,  
        "created_by" : 2,  
        "body" : "first comment"  
    },  
    {  
        "id" : 2,  
        "created_by" : 2,  
        "body" : "second comment",  
        "post" : 1  
    }  
    ]  
}  
```
  
### when i create a user instance manually in the admin app and i create a Token object manually also the login view work fine, but using the UserSerializer and UserCreate view the token does not created automatically and even if i create it (the token) manually in the django admin i can't login - the authenticat() method return None instead 
