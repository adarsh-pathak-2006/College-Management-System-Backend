from django.urls import path
from administration.views import *

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('department/', DepartmentAPI.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentAPI_individual.as_view(), name='department_individual'),
    path('course/', CourseAPI.as_view(), name='course'),
    path('course/<int:pk>/', CourseAPI_individual.as_view(), name='course_individual'),
    path('subject/', SubjectAPI.as_view(), name='subject'),
    path('subject/<int:pk>/', SubjectAPI_individual.as_view(), name='subject_individual'),
    path('notice/', NoticeAPI.as_view(), name='notice'),
    path('notice/<int:pk>/', NoticeAPI_individual.as_view(), name='notice_individual'),
    path('exam/', ExamAPI.as_view(), name='exam'),
    path('exam/<int:pk>/', ExamAPI_individual.as_view(), name='exam_individual'),
]