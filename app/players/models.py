from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.measure import D
from django.template.defaultfilters import slugify

BATS_CHOICES = (
    (True, "Right"),
    (False, "Left"),
    (None, "Switch"),
)

THROWS_CHOICES = (
    (True, "Right"),
    (False, "Left"),
)

class Player(models.Model):
    slug = models.SlugField(max_length=40)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born = models.DateField()
    positions = ArrayField(models.CharField(max_length=100), blank=True)
    bats = models.BooleanField(choices=BATS_CHOICES)
    throws = models.BooleanField(choices=THROWS_CHOICES)
    height = models.IntegerField(help_text="Centimeter")
    weight = models.IntegerField(help_text="Kilometer")
    retired = models.BooleanField(default=False)

    def measurement_format(self):
        return D(cm=self.height), D(km=self.weight)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + self.last_name)

        if not self.height or not self.weight:
            self.height, self.weight = self.measurement_format()


        self.measurement_format()
        return super().save(*args, **kwargs)