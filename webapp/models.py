from django.db import models


class ServicesSlider(models.Model):
    """Services slides model"""

    name = models.CharField(max_length=100, verbose_name='name', null=False)
    image = models.ImageField(upload_to='services_slider', verbose_name='photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services-Slider"
        verbose_name_plural = "Services-Slider"
