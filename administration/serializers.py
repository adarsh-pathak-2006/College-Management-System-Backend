from rest_framework.serializers import ModelSerializer
from administration.models import Department, Course, Subject, Notice
from django.contrib.auth.models import User
from teacher.serializers import TeacherSerializer
from administration.models import Exam

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model=Department
        fields=['name', 'code']


class CourseSerializer(ModelSerializer):
    department=DepartmentSerializer()
    class Meta:
        model=Course
        fields=['name', 'duration', 'department']

class SubjectSerializer(ModelSerializer):
    course=CourseSerializer()
    department=DepartmentSerializer()
    teacher=TeacherSerializer()
    class Meta:
        model=Subject
        fields=['name', 'code', 'teacher', 'course', 'department']


class NoticeSerializer(ModelSerializer):
    department=DepartmentSerializer()
    class Meta:
        model=Notice
        fields=['title', 'description', 'department', 'created_at']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'role']


class ExamSerializer(ModelSerializer):
    class Meta:
        model=Exam
        fields=['name', 'start_date', 'End_date']