from django.db import models

class Publisher(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Publisher Name'
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Publisher Country'
    )
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name='Publisher Website'
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name