from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class SnippetHomeView(TemplateView):
    template_name = "snippets/snippet-home.html"