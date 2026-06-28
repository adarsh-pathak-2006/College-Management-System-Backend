from rest_framework.serializers import ModelSerializer
from student.models import Student, Attendance
from administration.serializers import UserSerializer, CourseSerializer, DepartmentSerializer
from administration.serializers import SubjectSerializer
from teacher.serializers import TeacherSerializer


class StudentSerializer(ModelSerializer):
    user=UserSerializer()
    course=CourseSerializer()
    department=DepartmentSerializer()
    class Meta:
        model=Student
        fields=['user', 'rollno', 'phone', 'date_of_birth', 'gender', 'address', 'course', 'department', 'admission_date']


class AttendanceSerializer(ModelSerializer):
    student=StudentSerializer()
    subject=SubjectSerializer()
    teacher=TeacherSerializer()
    class Meta:
        model=Attendance
        fields='__all__'