from django.db import models
from django.conf import settings
from administration.models import Department
from administration.models import Exam, Subject


class Teacher(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacherid=models.CharField(max_length=15)
    name=models.CharField(max_length=150)
    email=models.EmailField()
    phoneno=models.CharField(max_length=15)
    qualification=models.CharField(max_length=150)
    salary=models.PositiveIntegerField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    joining_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacherid


class Result(models.Model):
    student=models.ForeignKey("student.Student", on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    marks=models.IntegerField()
    grade=models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.rollno} -- {self.student.course.name}"
