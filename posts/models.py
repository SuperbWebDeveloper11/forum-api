from django.db import models


class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, default='this article is empty')
    refined_body = models.TextField(blank=True, default='') 

    def save(self, *args, **kwargs):
        """
        Supose that we want to refine the body created by the user 
        in some format manually (markdown as an example) 
        """
        self.body_refined = self.body + ' - refined - '
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

