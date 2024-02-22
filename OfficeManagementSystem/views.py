from django.shortcuts import render,redirect
from owner.models import Owner
from employee.models import Employee,Department

def index(request):
    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')
        owner_data = Owner.objects.all()
        emp_data = Employee.objects.all()
        for i in owner_data:
            if i.emaill == email:
                if i.passwordd == passw:
                    return render(request, "owner.html")
                else : 
                    data = {'Message':'Please enter correct email/Password'}
                    return render(request, "index.html", data)
        for i in emp_data:
            if i.emaill == email:
                if i.passwordd == passw:
                    return render(request, "employee.html", {"pw":passw})
                else : 
                    data = {'Message':'Please enter correct email/Password'}
                    return render(request, "index.html", data)
        data = {'Message':'Please enter correct email/Password'}
        return render(request, "index.html", data)
    return render(request, "index.html")

def AllEmpDetails(request):
    emp_details = Employee.objects.all()
    data = {'Employee_Details':emp_details}
    if request.method=="POST":
        pw = request.POST.get('pw')
        emp = Employee.objects.get(passwordd=pw)
        emp_dept = emp.dept
        emp.delete()
        dept = Department.objects.get(dept_name=emp_dept)
        dept.no_of_employee -= 1
        dept.save()
        data["message"]=True
        return render(request, "AllEmpDetails.html", data)
    return render(request, "AllEmpDetails.html", data)

def AddEmp(request):
    dep = Department.objects.all()
    data = {"Dep":dep}
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passw = request.POST.get('passw')
        ph = request.POST.get('phone')
        emp = Employee.objects.all()
        for empp in emp:
            if empp.passwordd == passw:
                data["error"] = True
                return render(request, "AddEmp.html", data)
        addr = request.POST.get('addr')
        j_title = request.POST.get('j-title')
        sal = request.POST.get('sal')
        j_date = request.POST.get('j-date')
        depart_name = request.POST.get('dep')
        depart = Department.objects.get(dept_name=depart_name)
        employee = Employee(firstname=fname, lastname=lname, emaill=email, passwordd=passw, phone=ph, address=addr, job_title=j_title, salary=sal, joined_date=j_date, dept=depart)
        employee.save()
        department = Department.objects.get(dept_name=depart)
        department.no_of_employee += 1
        department.save()
        data["message"] = True
        return render(request, "AddEmp.html", data)
    return render(request, "AddEmp.html", data)

def EditEmp(request, pw):
    data = {}
    data["pw"] = pw
    employee = Employee.objects.get(passwordd=pw)
    old_dept = employee.dept
    data["emp"] = employee
    Dep = Department.objects.all()
    data["Dep"]=Dep
    if request.method=="POST":
        passw = request.POST.get('passw')
        if passw != employee.passwordd:
            emp = Employee.objects.all()
            for empp in emp:
                if empp.passwordd == passw:
                    data["error"] = True
                    return render(request, "EditEmp.html", data)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        ph = request.POST.get('phone')
        addr = request.POST.get('addr')
        j_title = request.POST.get('j-title')
        sal = request.POST.get('sal')
        j_date = request.POST.get('j-date')
        depart_name = request.POST.get('dep')
        new_dept = Department.objects.get(dept_name=depart_name)
        employee.firstname = fname
        employee.lastname = lname
        employee.emaill = email
        employee.passwordd = passw
        if pw!=passw:
            pw = passw
        employee.phone = ph
        employee.address = addr
        employee.job_title = j_title
        employee.salary = sal
        employee.joined_date = j_date
        if old_dept != new_dept:
            new_dept.no_of_employee += 1
            new_dept.save()
            last_dept = Department.objects.get(dept_name=employee.dept)
            last_dept.no_of_employee -= 1
            last_dept.save()
            employee.dept = new_dept
            UpdDep = Department.objects.all()
            data["Dep"]=UpdDep
        employee.save()
        upd_emp = Employee.objects.get(passwordd=passw)
        data["emp"] = upd_emp
        data["message"]=True
        return render(request, "EditEmp.html", data)
    return render(request, "EditEmp.html", data)

def AllDepartmentDetails(request):
    departments = Department.objects.all()
    data = {"Deps":departments}
    if request.method=="POST":
        DepName = request.POST.get("depname")
        Dep = Department.objects.get(dept_name=DepName)
        Dep.delete()
        data["message"] = True
        UpdDeps = Department.objects.all()
        data["Deps"] = UpdDeps
        return render(request, "AllDepartmentDetails.html", data)
    return render(request, "AllDepartmentDetails.html", data)

def AddDept(request):
    if request.method=="POST":
        data = {}
        DepName = request.POST.get("depname")
        deps = Department.objects.all()
        for dep in deps:
            if dep.dept_name == DepName:
                data["error"]=True
                return render(request, "AddDept.html", data)
        NewDept = Department(dept_name=DepName, no_of_employee=0)
        NewDept.save()
        data["message"]=True
        return render(request, "AddDept.html", data)
    return render(request, "AddDept.html")

def EditDept(request, depname):
    dep = Department.objects.get(dept_name=depname)
    data = {"dep":dep}
    if request.method=="POST":
        new_dept = request.POST.get("depname")
        if new_dept!=dep.dept_name:
            deps = Department.objects.all()
            for depart in deps:
                if depart.dept_name==new_dept:
                    data["error"]=True
                    return render(request, "EditDept.html", data)
            dep.dept_name = new_dept
            dep.save()
            data["message"]=True
            updata = Department.objects.all()
            data["dep"] = updata
            return render(request, "EditDept.html", data)
        return render(request, "EditDept.html", data)
    return render(request, "EditDept.html", data)

def ViewEmpDetails(request, passw):
    emp = Employee.objects.get(passwordd=passw)
    data = {"emp":emp}
    return render(request, "ViewEmpDetails.html", data)

def EditEmpDetails(request, passw):
    emp = Employee.objects.get(passwordd=passw)
    data = {}
    data["emp"] = emp
    data["pw"] = passw
    if request.method=="POST":
        pw = request.POST.get('passw')
        if pw != emp.passwordd:
            emps = Employee.objects.all()
            for empp in emps:
                if empp.passwordd == pw:
                    data["error"] = True
                    return render(request, "EditEmpDetails.html", data)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        ph = request.POST.get('phone')
        addr = request.POST.get('addr')
        emp.firstname = fname
        emp.lastname = lname
        emp.emaill = email
        emp.passwordd = passw
        if passw!=pw:
            passw = pw
        emp.phone = ph
        emp.address = addr
        emp.save()
        upd_emp = Employee.objects.get(passwordd=passw)
        data["emp"] = upd_emp
        data["message"]=True
        return render(request, "EditEmpDetails.html", data)
    return render(request, "EditEmpDetails.html", data)