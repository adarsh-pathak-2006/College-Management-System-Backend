from rest_framework.serializers import ModelSerializer
from teacher.models import Teacher
from administration.models import Department


class TeacherSerializer(ModelSerializer):
    department=Department.objects.all()
    class Meta:
        model=Teacher
        fields='__all__'