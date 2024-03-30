from django.db import models
from django.utils.html import format_html

# Create your models mean Table for your Database here.

# Category Model or Table

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;" />'.format(self.image))

    def __str__(self):
        return self.title

# Post Model or Table
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post/')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


