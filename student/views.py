from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Student, Attendance
from student.serializers import StudentSerializer, AttendanceSerializer
from administration.permissions import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


User = get_user_model()


class StudentAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsTeacherorAdmin()]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Student.objects.none()
        if user.role in [User.ADMIN, User.TEACHER]:
            return Student.objects.all()
        return Student.objects.filter(user=user)

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentAPI_Individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsStudentRelatedOrAdmin()]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AttendanceAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsTeacherorAdmin()]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Attendance.objects.none()
        if user.role in [User.ADMIN, User.TEACHER]:
            return Attendance.objects.all()
        return Attendance.objects.filter(student__user=user)

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAttendanceParticipantTeacherOrAdmin()]

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
