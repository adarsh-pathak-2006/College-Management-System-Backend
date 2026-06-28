from django.shortcuts import render
from accountant.serializers import FeeStructureSerializer, FeePaymentSerializer
from accountant.models import FeePayment, FeeStructure
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class FeePaymentAPI(ListCreateAPIView):
    queryset=FeePayment.objects.all()
    serializer_class=FeePaymentSerializer

class FeePayementAPI_Individual(RetrieveUpdateDestroyAPIView):
    queryset=FeePayment.objects.all()
    serializer_class=FeePaymentSerializer


class FeeStructureAPI(ListCreateAPIView):
    queryset=FeeStructure.objects.all()
    serializer_class=FeeStructureSerializer

class FeeStructureAPI_individual(RetrieveUpdateDestroyAPIView):
    queryset=FeeStructure.objects.all()
    serializer_class=FeeStructureSerializer