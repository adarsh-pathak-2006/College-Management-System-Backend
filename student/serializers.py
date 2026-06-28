from rest_framework.serializers import ModelSerializer
from student.models import Student, Attendance
from administration.serializers import UserSerializer, CourseSerializer, DepartmentSerializer
from administration.serializers import SubjectSerializer
from teacher.serializers import TeacherSerializer


class StudentSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    course=CourseSerializer(read_only=True)
    department=DepartmentSerializer(read_only=True)
    class Meta:
        model=Student
        fields=['user', 'rollno', 'phone', 'date_of_birth', 'gender', 'address', 'course', 'department', 'admission_date']


class AttendanceSerializer(ModelSerializer):
    student=StudentSerializer(read_only=True)
    subject=SubjectSerializer(read_only=True)
    teacher=TeacherSerializer(read_only=True)
    class Meta:
        model=Attendance
        fields='__all__'