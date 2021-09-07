from rest_framework import serializers
from .models import Employee


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at")
        model = Employee
