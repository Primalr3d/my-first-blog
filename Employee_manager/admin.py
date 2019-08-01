from django.contrib import admin

from Employee_manager.models import Employee, Group, Manager
# Register your models here.
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Manager)