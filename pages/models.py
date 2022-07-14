from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    author = models.CharField(blank=True, null=True, default='Anonymous Author', max_length=255)
    times_read = models.IntegerField(default=0)
    breaking = models.BooleanField(default=False)

    def __str__(self):
        return (self.title + str(self.timestamp))

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url