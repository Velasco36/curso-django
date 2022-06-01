import imp
from pydoc import classname
from re import I
import django
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from .models import Test
from .forms import TestForm

class TestView(TemplateView):
    template_name= 'home/test.html'

# Create your views here.

class ResumeForundationview(TemplateView):
    template_name = 'home/resume_foundation.html'

class Hometemplate1view(TemplateView):
    template_name = 'home/home1.html'


class Hometemplate2view(TemplateView):
    template_name = 'home/home2.html'


class Hometemplate2view(TemplateView):
    template_name = 'home/home2.html'

class TestListView(ListView):
    template_name = "home/list.html"
    context_object_name= 'Number_list'
    queryset= ['0','1','10','20','30']


class ListTest(ListView):
    template_name = "home/list_test.html"
    model = Test
    context_object_name= "list"


class TestCreateView(CreateView):    
    template_name = "home/add.html"
    model = Test
    form_class = TestForm
    success_url = '/'