from rest_framework.serializers import ModelSerializer
from teacher.models import Teacher, Result
from administration.serializers import DepartmentSerializer, SubjectSerializer, ExamSerializer, UserSerializer
from student.serializers import StudentSerializer



class TeacherSerializer(ModelSerializer):
    user=UserSerializer()
    department=DepartmentSerializer()
    class Meta:
        model=Teacher
        fields='__all__'


class ResultSerializer(ModelSerializer):
    student=StudentSerializer()
    subject=SubjectSerializer()
    exam=ExamSerializer()
    teacher=TeacherSerializer()
    class Meta:
        model=Result
        fields='__all__'