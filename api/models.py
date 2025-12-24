from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=55)
    location = models.CharField(max_length=65, blank=True, null=True)
    start_date = models.CharField(max_length=65)
    end_date = models.CharField(blank=True, null=True, max_length=65)
    description = models.CharField(blank=True, null=True, max_length=255)
    active = models.BooleanField(default=True)

class Medium(models.Model):
    title = models.CharField(max_length=55)

class Piece(models.Model):
    title = models.CharField(max_length=60)
    filename = models.CharField(max_length=60, blank=True, null=True)
    date = models.CharField(blank=True, null=True, max_length=65)
    description = models.CharField(max_length=255, blank=True, null=True)
    collections = models.ManyToManyField(Collection, related_name='collections', blank=True)
    media = models.ManyToManyField(Medium, related_name='media')
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    use_as_wallpaper = models.BooleanField(default=False)