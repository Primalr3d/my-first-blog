from django.urls import path
from Employee_manager import views

urlpatterns = [
    path('add/', views.add_employee_view),
    path('change/<int:employee_id>/group/<int:group_id>/', views.change_employee_view),
    path('group/<int:group_id>/', views.company_view),
    path('delete/<int:employee_id>/', views.delete_employee_view),
    path('', views.display_something),
]