from django.shortcuts import render
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer, ResultSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from teacher.models import Result
from administration.permissions import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


User = get_user_model()


class TeacherAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdmin()]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Teacher.objects.none()
        if user.role == User.ADMIN:
            return Teacher.objects.all()
        if user.role == User.TEACHER:
            return Teacher.objects.filter(user=user)
        return Teacher.objects.none()

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsTeacherOwnerOrAdmin()]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ResultAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsTeacherorAdmin()]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Result.objects.none()
        if user.role == User.ADMIN:
            return Result.objects.all()
        if user.role == User.TEACHER:
            return Result.objects.filter(teacher__user=user)
        return Result.objects.filter(student__user=user)

    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsResultParticipantTeacherOrAdmin()]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
