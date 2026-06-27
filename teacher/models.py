from django.db import models
from django.conf import settings
from administration.models import Department


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


