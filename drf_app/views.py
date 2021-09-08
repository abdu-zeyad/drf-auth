from rest_framework import generics
from .serializers import Employeeserializer
from .models import Employee
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class EmployeeList(generics.ListCreateAPIView):
    """
    List all posts.
    """

    queryset = Employee.objects.all()
    serializer_class = Employeeserializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single posts.
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
