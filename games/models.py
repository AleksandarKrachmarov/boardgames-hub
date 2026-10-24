from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from categories.models import Category
from publishers.models import Publisher


def validate_positive(value):
    if value <= 0:
        raise ValidationError('Value must be greater than 0')

class BoardGame(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Game Title',
    )
    min_players = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Min. Players'
    )
    max_players = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Max. Players'
    )
    play_time = models.IntegerField(
        validators=[validate_positive],
        verbose_name = "Play Time in Minutes"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Rating'
    )
    description = models.TextField(
        verbose_name='Game Description',
    )
    cover_image_url = models.URLField(
        verbose_name='Cover Image URL',
        blank=True,
        null=True,
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='games',
        verbose_name='Publisher',
    )
    categories = models.ManyToManyField(
        Category,
        related_name='games',
        verbose_name='Categories',
    )

    class Meta:
        ordering = ('-rating', 'title')

    def __str__(self):
        return self.title
