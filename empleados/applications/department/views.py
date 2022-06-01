import imp
from django.shortcuts import render
from django.views.generic.edit import FormView

#from empleados.applications import department
from .forms import NewDepartmentForms
from applications.person.models import Employee
from .models import Department
# Create your views here.

class NewDepartmentView(FormView):
    template_name = 'departmen/new_department.html'
    form_class = NewDepartmentForms
    success_url = '/'

    def form_valid(self, form):

        print('********** here **************')

        depa = Department(
            name=form.cleaned_data['department'],
            short_name=form.cleaned_data['shorname']    
        )
        depa.save()

        name=form.cleaned_data['name']
        last_name =form.cleaned_data['last_name']
        Employee.objects.create(
            first_name=name,
            last_name=last_name,
            job='1',
            department=depa
        )
        return super(NewDepartmentView, self).form_valid(form)
