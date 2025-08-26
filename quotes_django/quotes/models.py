from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .constants import (
    NAME_MAX_LENGTH,
    TYPE_MAX_LENGTH,
    TEXT_MAX_LENGTH,
    DEFAULT_WEIGTH,
    DEFAULT_LIKES,
    DEFAULT_VIEWS,
)


class Source(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    type = models.CharField(
        choices=[("book", "Книга"), ("movie", "Фильм")],
        max_length=TYPE_MAX_LENGTH,
    )


class Quote(models.Model):
    text = models.TextField(unique=True, max_length=TEXT_MAX_LENGTH)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(
        default=DEFAULT_WEIGTH,
        validators=[
            MinValueValidator(1, message="Вес не может быть меньше 1"),
            MaxValueValidator(10, message="Вес не может быть выше 10"),
        ],
    )
    views = models.PositiveIntegerField(default=DEFAULT_VIEWS)
    likes = models.PositiveIntegerField(default=DEFAULT_LIKES)
    dislikes = models.PositiveIntegerField(default=DEFAULT_LIKES)
    created_at = models.DateTimeField(auto_now_add=True)
