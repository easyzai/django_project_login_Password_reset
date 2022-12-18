from django.shortcuts import render, redirect
# from django.contrib.auth.forms import CreateUserForm
from .forms import EmployeeForm, CreateUserForm
from .models import Employee
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Show the employee list with restriction of the login
@login_required(login_url="login")
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


# Insert and update employee data with restriction of the login
@login_required(login_url="login")
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')


# delete the employee data with restricition
@login_required(login_url="login")
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')


# show and post the login user with redirection
def loginPanel(request):
    if request.user.is_authenticated:
        return redirect('employee_list')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')
            else:
                messages.info(request, "Username OR password is not correct")

        context = {}
        return render(request, "login.html", context)


# Logout user with restriction
@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect('login')


# Register the user with redirecting the route
def registerPanel(request):
    if request.user.is_authenticated:
        return redirect('employee_list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, "Account Created Successfully for "+user)
                return redirect('login')
        context = {'form': form}
        return render(request, "register.html", context)
