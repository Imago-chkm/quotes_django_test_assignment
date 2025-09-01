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
    """Модель источника цитаты, может быть книгой или фильмом."""

    name = models.CharField(
        max_length=NAME_MAX_LENGTH, unique=True, verbose_name="Название"
    )
    type = models.CharField(
        choices=[("book", "Книга"), ("movie", "Фильм")],
        max_length=TYPE_MAX_LENGTH,
        verbose_name="Тип источника",
    )

    class Meta:
        default_related_name = "source"
        verbose_name = "Источник"
        verbose_name_plural = "Источники"

    def __str__(self):
        return self.name


class Quote(models.Model):
    """Модель цитаты."""

    text = models.TextField("Текст", unique=True, max_length=TEXT_MAX_LENGTH)
    source = models.ForeignKey(
        Source, on_delete=models.CASCADE, verbose_name="Источник"
    )
    weight = models.PositiveIntegerField(
        "Вес цитаты от 1 до 10",
        default=DEFAULT_WEIGTH,
        validators=[
            MinValueValidator(1, message="Вес не может быть меньше 1"),
            MaxValueValidator(10, message="Вес не может быть выше 10"),
        ],
    )
    views = models.PositiveIntegerField("Просмотры", default=DEFAULT_VIEWS)
    likes = models.PositiveIntegerField("Лайки", default=DEFAULT_LIKES)
    dislikes = models.PositiveIntegerField("Дизлайки", default=DEFAULT_LIKES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "quotes"
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text[:50]
