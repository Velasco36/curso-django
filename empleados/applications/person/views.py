import imp
from turtle import update
from typing import Generic
from venv import create
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic import CreateView,TemplateView
from django.views.generic import UpdateView,DeleteView


#Models
from .models import Employee
#list view crear lista
class ListAllEmployee(ListView):
    template_name = "person/list_all.html"
    model = Employee
    paginate_by= 2
    ordering = 'first_name'

#error no me visualiza la lista
class ListByEmployee(ListView):
    #LIst of employee
    template_name = 'person/list_by_area.html'
    def get_queryset(self):
        area = self.kwargs['shorname']
        list = Employee.objects.filter(
            Deparment__shor_name='Otro'
        )
        return list

#error (no me aparece la lista)
class ListEmployeeByKword(ListView):
    template_name = "person/by_kword.html"
    context_object_name = 'Employee'

    def get_queryset(self):
        print('***********')
        key_word = self.request.GET.get("kword", '')
        list = Employee.objects.filter(
            first_name= key_word
        )  
        return list

class Listskills(ListView):
    template_name = 'person/skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        employee = Employee.objects.get(id=2)
        print(employee.skills.all())
        return employee.skills.all()
    

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "person/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView,self).get_context_data(**kwargs)
        context['title'] = 'Employee of month'
        return context
    

#create register data base
#import djaneiro (Extension DJANGO )


class SuccessView(TemplateView):
    template_name = "person/success.html"

class beginningview(TemplateView):
    "begginning"
    template_name= 'beginning.html'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "person/employee.html"
    fields= [
        'first_name',
        'last_name',
        'job', 
        'Department',
        'skills']
    success_url = reverse_lazy('Person_app:success')
    
    def form_valid(self, form):
        #logica del proceso
        employee= form.save(commit=False)
        print(employee)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)

# updateview to add form delete (modific) sin decesidad de ser admin 


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "person/update.html"
    fields= [
        'first_name',
        'last_name',
        'job', 
        'Department',
        'skills'
    ]
    success_url = reverse_lazy('Person_app:update')
    def post(self,requet, *args, **kwargs):
        self.object = self.get_object()
        print('***********method PSOT ***********')
        print('***********************************+')
        print(requet.POST)
        print(requet.PSOT['last_name'])
        return super().post(requet,*args, **kwargs)

    def form_valid(self, form):
        #logica del proceso
        print('===============Method form valid ============')
        print('************************************************')
        return super(EmployeeUpdateView).form_valid(form)


#delete at database
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "person/delete.html"
    success_url = reverse_lazy('Person_app:success')







