from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Student, Attendance
from student.serializers import StudentSerializer, AttendanceSerializer


class StudentAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentAPI_Individual(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class AttendanceAPI(ListCreateAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

class AttendanceAPI_individual(RetrieveUpdateDestroyAPIView):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer