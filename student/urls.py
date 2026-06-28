from django.urls import path
from student.views import *

urlpatterns=[
    path('', StudentAPI.as_view(), name='student_list'),
    path('<int:pk>/', StudentAPI_Individual.as_view(), name='student_detail'),
    path('attendance/', AttendanceAPI.as_view(), name='attendance_list'),
    path('attendance/<int:pk>/', AttendanceAPI_individual.as_view(), name='attendance_detail'),
]
