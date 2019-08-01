from django import forms
from Employee_manager.models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=255, help_text="Please enter the Employee's name.")
    group = forms.CharField(max_length=255, help_text="Please enter the Employee's company.")
    manager = forms.CharField(max_length=255, help_text="Please enter the Manager's name.")

    class Meta:
        model = Employee
        fields = ('name', 'group', 'manager')