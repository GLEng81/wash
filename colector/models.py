from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=128, unique=True, primary_key=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Stations'

    def __str__(self):
        return self.name


class Error(models.Model):
    station = models.ForeignKey(Station)
    msg = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.msg


class OnlineStations(models.Model):
    station = models.ForeignKey(Station, unique=True)
    last_request = models.DateTimeField(auto_now=True)
    new_config = models.BooleanField(default=False)
    info = models.CharField(max_length=128)

    def __str__(self):
        return str(self.last_request)

    class Meta:
        verbose_name_plural = 'OnlineStatitions'


class NewConfig(models.Model):
    station = models.ForeignKey(Station, unique=True)
    is_get = models.BooleanField(default=False)
    out1 = models.IntegerField(default=0)
    out2 = models.IntegerField(default=0)
    out3 = models.IntegerField(default=0)
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'New Config'


class Emails(models.Model):
    station = models.ForeignKey(Station)
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Email'