from django.contrib import admin
from .models import Employee, Skills

# Register your models here.
admin.site.register(Skills)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'Department',
        'job',
        'full_name',
        'id',

    )

    def full_name(self,obj):
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    search_fields= ('first_name',)
    list_filter = ('job','skills')

    filter_horizontal = ('skills',)

admin.site.register(Employee, EmployeeAdmin)

