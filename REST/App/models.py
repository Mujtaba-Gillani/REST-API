from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title