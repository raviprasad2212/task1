from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from .serializers import StudentsSerializsers
from .models import Students

def show(request):
    queryset = Students.objects.all()
    serail_data = StudentsSerializsers(queryset, many=True)
    return JSONRenderer().render(serail_data.data)