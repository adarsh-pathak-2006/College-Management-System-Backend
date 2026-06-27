from django.shortcuts import render
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class TeacherAPI(ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

class TeacherAPI_individual(RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

