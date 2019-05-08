from django.db import models
from django.utils import timezone
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    display = models.BooleanField(default=False)
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:album', args=[self.slug])

class AlbumImage(models.Model):
    name = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100)