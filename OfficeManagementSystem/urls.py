"""
URL configuration for OfficeManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('AllEmpDetails/', views.AllEmpDetails, name="AllEmpDetails"),
    path('AllEmpDetails/AddEmp/', views.AddEmp, name="AddEmp"),
    path('AllEmpDetails/EditEmp/<str:pw>/', views.EditEmp, name="EditEmp"),
    path('AllDepartmentDetails/', views.AllDepartmentDetails, name="AllDepartmentDetails"),
    path('AllDepartmentDetails/AddDept/', views.AddDept, name="AddDept"),
    path('AllDepartmentDetails/EditDept/<str:depname>/', views.EditDept, name="EditDept"),
    path('ViewEmpDetails/<str:passw>/', views.ViewEmpDetails, name="ViewEmpDetails"),
    path('EditEmpDetails/<str:passw>/', views.EditEmpDetails, name="EditEmpDetails")
]
