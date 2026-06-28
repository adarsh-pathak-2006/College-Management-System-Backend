from django.shortcuts import render
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer, ResultSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from teacher.models import Result



class TeacherAPI(ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

class TeacherAPI_individual(RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

class Result(ListCreateAPIView):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer