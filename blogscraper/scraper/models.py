from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=80)
    blog_url = models.URLField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    subscribers = models.IntegerField()
    blog_picture = models.ImageField(default='images/ubuntu_orange.png')    
    def __str__(self):
        return self.blog_name

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    date_added = models.DateField(auto_now=True)
    blog_title = models.CharField(max_length=80)
    blog_text = models.TextField(max_length=99999)
    blog_picture = models.ImageField(default='images/ubuntu_orange.png')

    def __str__(self):
        return self.blog_title

    def is_long_post(self):
        if len(self.blog_text) >= 3000:
            return True
        else:
            return False