from django.db import models
from django.conf import settings
from administration.models import Department, Course
from administration.models import Subject


class Student(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rollno=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    admission_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rollno
    

class Attendance(models.Model):
    PRESENT = "P"
    ABSENT = "A"
    LEAVE = "L"

    STATUS_CHOICES = [
        (PRESENT, "Present"),
        (ABSENT, "Absent"),
        (LEAVE, "Leave"),
    ]

    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher=models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        unique_together=('student', 'subject', 'date')


    def __str__(self):
        return str(self.date)
