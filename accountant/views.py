from django.shortcuts import render
from accountant.serializers import FeeStructureSerializer, FeePaymentSerializer
from accountant.models import FeePayment, FeeStructure
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from administration.permissions import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


User = get_user_model()


class FeePaymentAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminorAccountant()]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return FeePayment.objects.none()
        if user.role in [User.ADMIN, User.ACCOUNTANT]:
            return FeePayment.objects.all()
        return FeePayment.objects.filter(student__user=user)

    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer


class FeePayementAPI_Individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsFeePaymentOwnerAccountantOrAdmin()]

    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer


class FeeStructureAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdmin()]

    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer


class FeeStructureAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdmin()]

    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
