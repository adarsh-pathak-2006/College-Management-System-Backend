from django.db import models
from django.conf import settings
from administration.models import Department, Course


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
    