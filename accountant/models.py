from django.db import models
from administration.models import Course, Semester


class FeeStructure(models.Model):
    course=models.OneToOneField(Course, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return self.course.name

class FeePayment(models.Model):
    PAID="PAID"
    PENDING="PENDING"
    PARTIAL="PARTIAL"
    STATUS_CHOICES=[(PAID, 'paid'),(PENDING,'pending'),(PARTIAL, 'partial')]

    student=models.ForeignKey("student.Student", on_delete=models.CASCADE)
    feestructure=models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    amount_paid=models.PositiveIntegerField()
    payment_date=models.DateField()
    transactionid=models.CharField(max_length=50, null=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.student.rollno
