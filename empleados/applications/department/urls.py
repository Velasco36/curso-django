from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.NewDepartmentView.as_view(), name='new'),


]