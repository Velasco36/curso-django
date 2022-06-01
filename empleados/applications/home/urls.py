from django.urls import path
from . import views



urlpatterns = [
    path('test/', views.TestView.as_view()),
    path('list/', views.TestListView.as_view()),
    path('list_test/', views.ListTest.as_view()),
    path('add/',views.TestCreateView.as_view(), name="add-test"),
    path('found/',views.ResumeForundationview.as_view(), name="resumen"),
    path('home1/',views.ResumeForundationview.as_view(), name="home1"),
    path('home2/',views.ResumeForundationview.as_view(), name="home2"),
    path('home3/',views.ResumeForundationview.as_view(), name="home3"),
]