from rest_framework.serializers import ModelSerializer
from accountant.models import FeePayment, FeeStructure
from administration.serializers import CourseSerializer, Semester_serializer
from student.serializers import StudentSerializer


class FeeStructureSerializer(ModelSerializer):
    course=CourseSerializer()
    semester=Semester_serializer()
    class Meta:
        model=FeeStructure
        fields='__all__'

class FeePaymentSerializer(ModelSerializer):
    student=StudentSerializer()
    feestructure=FeeStructureSerializer()
    class Meta:
        model=FeePayment
        fields='__all__'