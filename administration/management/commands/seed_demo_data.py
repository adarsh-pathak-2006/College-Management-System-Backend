from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from administration.models import Course, Department, Exam, Notice, Semester, Subject
from accountant.models import FeePayment, FeeStructure
from student.models import Attendance, Student
from teacher.models import Result, Teacher


class Command(BaseCommand):
    help = "Create repeatable demo data for the college management app."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=20,
            help="Number of records to create for each seeded model.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        count = options["count"]
        if count < 1:
            self.stderr.write("count must be at least 1")
            return

        User = get_user_model()

        departments = []
        for index in range(1, count + 1):
            department, _ = Department.objects.update_or_create(
                code=f"D{index:02d}",
                defaults={
                    "name": f"Department {index}",
                },
            )
            departments.append(department)

        courses = []
        for index in range(1, count + 1):
            department = departments[(index - 1) % len(departments)]
            course, _ = Course.objects.update_or_create(
                name=f"Course {index}",
                defaults={
                    "duration": 2 + (index % 4),
                    "department": department,
                },
            )
            courses.append(course)

        semesters = []
        for index, course in enumerate(courses, start=1):
            semester, _ = Semester.objects.update_or_create(
                course=course,
                number=((index - 1) % 8) + 1,
                session=f"202{index % 10}-202{(index + 1) % 10}",
                defaults={
                    "isactive": index == 1,
                },
            )
            semesters.append(semester)

        admin_user, _ = User.objects.update_or_create(
            username="seed_admin",
            defaults={
                "first_name": "Seed",
                "last_name": "Admin",
                "email": "seed.admin@example.com",
                "role": User.ADMIN,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin_user.set_password("password123")
        admin_user.save()

        accountant_user, _ = User.objects.update_or_create(
            username="seed_accountant",
            defaults={
                "first_name": "Seed",
                "last_name": "Accountant",
                "email": "seed.accountant@example.com",
                "role": User.ACCOUNTANT,
                "is_staff": True,
                "is_superuser": False,
            },
        )
        accountant_user.set_password("password123")
        accountant_user.save()

        teachers = []
        for index in range(1, count + 1):
            user, _ = User.objects.update_or_create(
                username=f"seed_teacher_{index:02d}",
                defaults={
                    "first_name": f"Teacher{index}",
                    "last_name": "Seed",
                    "email": f"teacher{index:02d}@example.com",
                    "role": User.TEACHER,
                    "is_staff": False,
                    "is_superuser": False,
                },
            )
            user.set_password("password123")
            user.save()

            teacher, _ = Teacher.objects.update_or_create(
                teacherid=f"TCH{index:03d}",
                defaults={
                    "user": user,
                    "name": f"Teacher {index}",
                    "email": f"teacher{index:02d}@example.com",
                    "phoneno": f"900000{index:04d}",
                    "qualification": "M.Ed",
                    "salary": 40000 + (index * 750),
                    "department": departments[(index - 1) % len(departments)],
                },
            )
            teachers.append(teacher)

        subjects = []
        for index in range(1, count + 1):
            course = courses[(index - 1) % len(courses)]
            subject, _ = Subject.objects.update_or_create(
                code=f"SUB{index:03d}",
                defaults={
                    "name": f"Subject {index}",
                    "course": course,
                    "department": course.department,
                },
            )
            subject.teacher.set([teachers[(index - 1) % len(teachers)]])
            subjects.append(subject)

        notices = []
        for index in range(1, count + 1):
            notice, _ = Notice.objects.update_or_create(
                title=f"Notice {index}",
                defaults={
                    "description": f"This is seed notice number {index}.",
                    "department": departments[(index - 1) % len(departments)],
                },
            )
            notices.append(notice)

        exams = []
        exam_start = date(2026, 1, 5)
        for index in range(1, count + 1):
            exam, _ = Exam.objects.update_or_create(
                name=f"Exam {index}",
                defaults={
                    "start_date": exam_start + timedelta(days=index * 7),
                    "End_date": exam_start + timedelta(days=index * 7 + 5),
                },
            )
            exams.append(exam)

        students = []
        student_base_date = date(2004, 1, 1)
        for index in range(1, count + 1):
            user, _ = User.objects.update_or_create(
                username=f"seed_student_{index:02d}",
                defaults={
                    "first_name": f"Student{index}",
                    "last_name": "Seed",
                    "email": f"student{index:02d}@example.com",
                    "role": User.STUDENT,
                    "is_staff": False,
                    "is_superuser": False,
                },
            )
            user.set_password("password123")
            user.save()

            course = courses[(index - 1) % len(courses)]
            student, _ = Student.objects.update_or_create(
                rollno=f"R{index:04d}",
                defaults={
                    "user": user,
                    "phone": f"888880{index:04d}",
                    "date_of_birth": student_base_date + timedelta(days=index * 31),
                    "gender": "Male" if index % 2 else "Female",
                    "address": f"{index} Seed Street, Campus City",
                    "course": course,
                    "department": course.department,
                },
            )
            students.append(student)

        fee_structures = []
        for index, course in enumerate(courses, start=1):
            fee_structure, _ = FeeStructure.objects.update_or_create(
                course=course,
                defaults={
                    "semester": semesters[(index - 1) % len(semesters)],
                    "amount": 30000 + (index * 1000),
                },
            )
            fee_structures.append(fee_structure)

        for index, student in enumerate(students, start=1):
            subject = subjects[(index - 1) % len(subjects)]
            teacher = teachers[(index - 1) % len(teachers)]
            exam = exams[(index - 1) % len(exams)]
            fee_structure = fee_structures[(index - 1) % len(fee_structures)]

            Attendance.objects.update_or_create(
                student=student,
                subject=subject,
                date=date(2026, 2, 1) + timedelta(days=index),
                defaults={
                    "teacher": teacher,
                    "status": [Attendance.PRESENT, Attendance.ABSENT, Attendance.LEAVE][index % 3],
                },
            )

            Result.objects.update_or_create(
                student=student,
                subject=subject,
                exam=exam,
                defaults={
                    "teacher": teacher,
                    "marks": 55 + (index % 45),
                    "grade": ["A", "B", "C", "D"][index % 4],
                },
            )

            FeePayment.objects.update_or_create(
                transactionid=f"TXN{index:05d}",
                defaults={
                    "student": student,
                    "feestructure": fee_structure,
                    "amount_paid": 15000 + (index * 500),
                    "payment_date": date(2026, 3, 1) + timedelta(days=index),
                    "status": [FeePayment.PAID, FeePayment.PENDING, FeePayment.PARTIAL][index % 3],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {count} departments, courses, semesters, teachers, subjects, notices, exams, students, attendance rows, results, fee structures, and fee payments."
            )
        )
