from django.db import models
from django.urls import reverse



class Post(models.Model):
    owner = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-updatetime']

    def get_absolute_url(self):
        return reverse ('home')
        