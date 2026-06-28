from rest_framework.serializers import ModelSerializer
from teacher.models import Teacher, Result

class TeacherSerializer(ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        from administration.serializers import DepartmentSerializer, UserSerializer

        data['user'] = UserSerializer(instance.user).data
        data['department'] = DepartmentSerializer(instance.department).data
        return data


class ResultSerializer(ModelSerializer):
    class Meta:
        model=Result
        fields='__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        from administration.serializers import ExamSerializer, SubjectSerializer
        from student.serializers import StudentSerializer

        data['student'] = StudentSerializer(instance.student).data
        data['subject'] = SubjectSerializer(instance.subject).data
        data['exam'] = ExamSerializer(instance.exam).data
        data['teacher'] = TeacherSerializer(instance.teacher).data
        return data
