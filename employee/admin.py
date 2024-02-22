from django.contrib import admin
from django.contrib.admin.sites import site
from employee.models import Department, Employee

class MyDepAdmin(admin.ModelAdmin):
    list_display = ('dept_name','no_of_employee')
    
class MyEmpAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','emaill','passwordd','phone','address','job_title','salary','joined_date','dept')
    
admin.site.register(Department, MyDepAdmin)
admin.site.register(Employee, MyEmpAdmin)
# Register your models here.
