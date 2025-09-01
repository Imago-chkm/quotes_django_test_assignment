from django.contrib import admin
from .models import Source, Quote


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)
    search_fields = ("name",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "text_short",
        "source",
        "weight",
        "likes",
        "dislikes",
        "views",
        "created_at",
    )
    list_filter = ("source__type", "created_at")
    search_fields = ("text",)
    readonly_fields = ("views", "created_at")

    @admin.display(description="Текст")
    def text_short(self, obj):
        return obj.text[:50]
