from django import forms

class NewDepartmentForms(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    