from django.urls import path
from teacher.views import *

urlpatterns=[
    path('', TeacherAPI.as_view(), name='teacher'),
    path('<int:pk>/', TeacherAPI_individual.as_view(), name='teacher_individual'),
    path('result/', ResultAPI.as_view(), name='result'),
    path('result/<int:pk>/', ResultAPI_individual.as_view(), name='result_individual'),
]