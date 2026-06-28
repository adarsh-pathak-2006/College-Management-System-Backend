from django.urls import path
from accountant.views import *

urlpatterns=[
    path('structure/', FeeStructureAPI.as_view(), name='feestructure'),
    path('structure/<int:pk>/', FeeStructureAPI_individual.as_view(), name='feestructure_individual'),
    path('payment/', FeePaymentAPI.as_view(), name='feepayment'),
    path('payment/<int:pk>/', FeePaymentAPI.as_view(), name='feepayment_individual'),
]