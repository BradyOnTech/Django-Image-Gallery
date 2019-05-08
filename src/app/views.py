from django.shortcuts import render, get_object_or_404
from .models import Album, AlbumImage

def home(request):
    top_albums = Album.objects.filter(display=True).order_by('published_date')[:3]
    bottom_albums = Album.objects.filter(display=True).order_by('-published_date')[:2]
    return render(request, 'app/home.html', {'top_albums': top_albums, 'bottom_albums': bottom_albums})

def album(request, slug):
    images = AlbumImage.objects.filter(album__slug=slug)
    return render(request, 'app/album_detail.html', {'images': images})
