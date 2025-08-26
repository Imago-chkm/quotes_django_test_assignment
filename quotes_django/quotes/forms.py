from django import forms

from .models import Quote


class QuoteForm(forms.ModelForm):
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
