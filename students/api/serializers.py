from .models import Students
# Create your views here.
from rest_framework import serializers

class StudentsSerializsers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"