from django.shortcuts import render, redirect, get_object_or_404

from employee.models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    context ={
        'employees': employees
    }
    return render(request, 'employee/employee_list.html', context)
    
def employee_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')

        employee = Employee()
        employee.name = name
        employee.position = position
        employee.save()

        return redirect('employee:employee_list')
    return render(request, 'employee/employee_create.html')

def employee_update(request,pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.position = request.POST.get('position')
        employee.save()
        return redirect('employee:employee_list')
    context = {
        'employee': employee
    }
    return render(request, 'employee/employee_edit.html', context)

def employee_delete(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee:employee_list')
    context = {
        'employee': employee
    }

    return render(request, 'employee/employee_delete.html',context)