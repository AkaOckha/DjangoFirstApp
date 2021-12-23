from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
        
        ordering = ['-published_date']