from django.contrib import admin
from django.core.files.base import ContentFile
from django.db import models
import gallery.settings
import zipfile
from PIL import Image
from app.forms import AlbumForm
from .models import Album, AlbumImage

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

    form = AlbumForm

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save(commit=False)
            album.save()

           
            file = zipfile.ZipFile(form.cleaned_data['file'])
            for image in sorted(file.namelist()):
                print(image)
                data = file.read(image)
                contentFile = ContentFile(data)

                img = AlbumImage()
                img.album = album
                
                for i in sorted(file.namelist()):
                    img.name = '{0}-{1}.jpg'.format(album.slug, i)
                    name = img.name
                img.image.save(name, contentFile)

                path = '{0}/albums/{1}'.format(gallery.settings.MEDIA_ROOT, name)
                with Image.open(path) as i:
                    img.width, img.height = i.size

                img.thumb.save('thumb-{0}'.format(name), contentFile)
                img.save()
            file.close()
        super(AlbumAdmin, self).save_model(request, obj, form, change)

class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'created')
    list_filter = ('name', 'album', 'created')


admin.site.register(Album,AlbumAdmin)
admin.site.register(AlbumImage,AlbumImageModelAdmin)