from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN='ADMIN'
    TEACHER='TEACHER'
    STUDENT='STUDENT'
    ACCOUNTANT='ACCOUNTANT'

    ROLE_CHOICES=[
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (ACCOUNTANT, 'Accountant'),
        (STUDENT, 'Student'),
    ]

    role=models.CharField(max_length=20, choices=ROLE_CHOICES)

class Department(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=5)


    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=150)
    duration=models.PositiveIntegerField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name=models.CharField(max_length=150)
    code=models.CharField(max_length=10)
    teacher=models.ManyToManyField("teacher.Teacher")
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    department=models.OneToOneField(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

class Notice(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
