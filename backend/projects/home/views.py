from typing import Any, Dict, List
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView



class HomePage(TemplateView):
    # template_name="home/homepage.html"
    def get_template_names(self):
        if self.request.user.is_authenticated:
            self.template_name = "home/loggedin-homepage.html"
        else:
            self.template_name = "home/homepage.html"
        return super().get_template_names()
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context =  super().get_context_data(**kwargs)
    #     if self.request.user.is_authenticated:
    #         self.template_name = "home/loggedin-homepage.html"
    #     else:
    #         self.template_name = "home/homepage.html"
    #     return context

