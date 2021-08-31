from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from .serializers import StudentsSerializsers
from .models import Students
from django.http import HttpResponse

def show(request):
    queryset = Students.objects.all()
    serail_data = StudentsSerializsers(queryset, many=True)
    final_data = JSONRenderer().render(serail_data.data)
    return HttpResponse(final_data)