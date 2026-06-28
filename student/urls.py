from django.urls import path
from student.views import *

urlpatterns=[
    path('', StudentAPI.as_view(), name='student'),
    path('<int:pk>/', StudentAPI_Individual.as_view(), name='student'),
]