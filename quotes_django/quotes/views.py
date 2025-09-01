from random import choices
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from .models import Quote, Source
from .forms import QuoteForm, SourceForm


class RandomQuoteView(TemplateView):
    template_name = "quotes/random.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Quote.objects.all()
        if qs:
            quote = choices(qs, weights=[q.weight for q in qs])[0]
            quote.views += 1
            quote.save()
            ctx["quote"] = quote
        return ctx


class PopularQuotesView(ListView):
    model = Quote
    template_name = "quotes/popular.html"
    queryset = Quote.objects.order_by("-likes")[:10]
    context_object_name = "quotes"


class AddQuoteView(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = "quotes/add_quote.html"
    success_url = "/"


def vote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "like":
            quote.likes += 1
        elif action == "dislike":
            quote.dislikes += 1
        quote.save()
    return redirect("quotes:random")


class AddSourceView(CreateView):
    model = Source
    form_class = SourceForm
    template_name = "quotes/add_source.html"

    def get_success_url(self):
        return self.request.GET.get("next", "/")
