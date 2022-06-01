from django.urls import path
from . import views

app_name = "Person_app"





urlpatterns = [
    path('', views.beginningview.as_view(), name="beginning"),
    path('list-all-employee/', views.ListAllEmployee.as_view(), name="list-all"),
    path('list-area/<shortname>/',views.ListByEmployee.as_view(), name="list-area"),
    path('key-word/',views.ListEmployeeByKword.as_view(), name="key-word"),
    path('list-skills/',views.Listskills.as_view(), name="list-skills"),
    path('detail/<pk>/',views.EmployeeDetailView.as_view(), name="detail"),
    path('add-employee/',views.EmployeeCreateView.as_view(),name = "add-employe"),
    path('success/',views.SuccessView.as_view(), name = 'success'),
    path('update-employee/<pk>/',views.EmployeeUpdateView.as_view(), name = 'update'),
    path('delete/<pk>/',views.EmployeeDeleteView.as_view(), name = 'delete'),
]