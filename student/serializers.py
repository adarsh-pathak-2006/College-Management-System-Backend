from rest_framework.serializers import ModelSerializer
from student.models import Student
from administration.serializers import UserSerializer, CourseSerializer, DepartmentSerializer

class StudentSerializer(ModelSerializer):
    user=UserSerializer()
    course=CourseSerializer()
    department=DepartmentSerializer()
    class Meta:
        model=Student
        fields=['user', 'rollno', 'name', 'email', 'phone', 'date_of_birth', 'gender', 'address', 'course', 'department' 'admission_date']
