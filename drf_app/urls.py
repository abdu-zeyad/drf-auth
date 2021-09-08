from django.urls import path
from .views import EmployeeDetail, EmployeeList

urlpatterns = [
    path("", EmployeeList.as_view(), name="post_list"),
    path("<int:pk>/", EmployeeDetail.as_view(), name="post_detail"),
]
