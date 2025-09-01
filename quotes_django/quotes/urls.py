from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.RandomQuoteView.as_view(), name="random"),
    path("popular/", views.PopularQuotesView.as_view(), name="popular"),
    path("add/", views.AddQuoteView.as_view(), name="add_quote"),
    path("source/add/", views.AddSourceView.as_view(), name="add_source"),
    path("quote/<int:pk>/vote/", views.vote, name="vote"),
]
