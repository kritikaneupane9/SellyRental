from django.shortcuts import render


from employee.models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'home.html',{'employees':employees})
    
