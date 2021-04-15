from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.measure import D
from django.template.defaultfilters import slugify

BATS_CHOICES = (
    ("Right", "Right"),
    ("Left", "Left"),
    ("Switch", "Switch"),
)

THROWS_CHOICES = (
    ("Right", "Right"),
    ("Left", "Left"),
)

class Player(models.Model):
    slug = models.SlugField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born = models.DateField()
    positions = ArrayField(models.CharField(max_length=100), default=list)
    bats = models.CharField(choices=BATS_CHOICES, max_length=50)
    throws = models.CharField(choices=THROWS_CHOICES, max_length=50)
    height = models.IntegerField(help_text="Centimeter")
    weight = models.IntegerField(help_text="Kilometer")
    retired = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + self.last_name)

        return super().save(*args, **kwargs)