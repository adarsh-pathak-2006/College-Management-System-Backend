from rest_framework.serializers import ModelSerializer
from accountant.models import FeePayment, FeeStructure
from administration.serializers import CourseSerializer, Semester_serializer
from student.serializers import StudentSerializer


class FeeStructureSerializer(ModelSerializer):
    course=CourseSerializer(read_only=True)
    semester=Semester_serializer(read_only=True)
    class Meta:
        model=FeeStructure
        fields='__all__'

class FeePaymentSerializer(ModelSerializer):
    student=StudentSerializer(read_only=True)
    feestructure=FeeStructureSerializer(read_only=True)
    class Meta:
        model=FeePayment
        fields='__all__'