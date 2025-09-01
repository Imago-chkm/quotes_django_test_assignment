from django import forms

from .models import Quote, Source


class QuoteForm(forms.ModelForm):
    """
    Форма для валидации цитат:
    - цитата не может иметь дубликатов
    - у одного источника не может быть более трех цитат
    """

    class Meta:
        model = Quote
        fields = ["text", "source", "weight"]

    def clean(self):
        source = self.cleaned_data.get("source")
        if source and Quote.objects.filter(source=source).count() >= 3:
            raise forms.ValidationError("У источника уже есть 3 цитаты")
        text = self.cleaned_data.get("text")
        if Quote.objects.filter(text=text).exists():
            raise forms.ValidationError("Такая цитата уже существует")
        return self.cleaned_data


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["name", "type"]
