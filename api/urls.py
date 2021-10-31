from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListEmployeeAPIView.as_view(),name="employee_list"),
    path("create/", views.CreateEmployeeAPIView.as_view(),name="employee_create"),
    path("update/<int:pk>/",views.UpdateEmployeeAPIView.as_view(),name="employee_update"),
    path("delete/<int:pk>/",views.DeleteEmployeeAPIView.as_view(),name="employee_delete")
]