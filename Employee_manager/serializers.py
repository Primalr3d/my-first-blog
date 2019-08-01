from rest_framework import serializers
from Employee_manager.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'group', 'manager']
