from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class TextUtilsHomepage(LoginRequiredMixin, TemplateView):
    template_name = "textutils/main.html"