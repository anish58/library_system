from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    context={

    }
    return render(request, 'main/index.html', context)

class Index(TemplateView):
    template_name = r"main\index.html"