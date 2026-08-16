from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from my_app.models import (
    SchoolClass,
    Students,
    Teachers,
    Subjects,
    Attendence,
    Marks,
    Parents,
)


class Command(BaseCommand):
    help = "Create demo data for the Student Management System"

    def handle(self, *args, **kwargs):

        self.stdout.write("Creating demo data...")

        # -------------------------------------------------
        # 1. CLASSES
        # -------------------------------------------------

        classes_data = [
            ("9", "A", "101"),
            ("9", "B", "102"),
            ("10", "A", "103"),
            ("10", "B", "104"),
            ("11", "A", "105"),
        ]

        school_classes = []

        for school_class, section, room_no in classes_data:
            obj, created = SchoolClass.objects.get_or_create(
                school_class=school_class,
                section=section,
                defaults={
                    "room_no": room_no,
                },
            )

            school_classes.append(obj)

        self.stdout.write(
            self.style.SUCCESS("5 classes ready.")
        )

        # -------------------------------------------------
        # 2. TEACHERS
        # -------------------------------------------------

        teachers_data = [
            ("Demo Teacher 01", "demo_teacher01"),
            ("Demo Teacher 02", "demo_teacher02"),
            ("Demo Teacher 03", "demo_teacher03"),
            ("Demo Teacher 04", "demo_teacher04"),
            ("Demo Teacher 05", "demo_teacher05"),
        ]
    
        teachers = []

        for fullname, username in teachers_data:

            user, created = User.objects.get_or_create(
                username=username,
            )

            if created:
                user.set_password("Demo@12345")
                user.save()

            teacher, created = Teachers.objects.get_or_create(
                user=user,
                defaults={
                    "fullname": fullname,
                    "email": f"{username}@example.com",
                    "phone": "03000000000",
                    "qualification": "BS Computer Science",
                },
            )

            teachers.append(teacher)

        self.stdout.write(
            self.style.SUCCESS("5 teachers ready.")
        )

        # -------------------------------------------------
        # 3. SUBJECTS
        # -------------------------------------------------

        subject_names = [
            "English",
            "Mathematics",
            "Science",
            "Computer",
        ]

        subjects = []

        for index, school_class in enumerate(school_classes):

            teacher = teachers[index]

            for subject_name in subject_names:

                subject, created = Subjects.objects.get_or_create(
                    subject_name=subject_name,
                    school_class=school_class,
                    defaults={
                        "teacher": teacher,
                    },
                )

                subjects.append(subject)

        self.stdout.write(
            self.style.SUCCESS("20 subjects ready.")
        )

        # -------------------------------------------------
        # 4. STUDENTS + STUDENT USERS
        # -------------------------------------------------

        students = []

        student_number = 1

        for school_class in school_classes:

            for i in range(3):

                username = f"demo_student{student_number:02d}"

                user, created = User.objects.get_or_create(
                    username=username,
                )

                if created:
                    user.set_password("Demo@12345")
                    user.save()

                student, created = Students.objects.get_or_create(
                    roll_no=9000 + student_number,
                    defaults={
                        "name": f"Demo Student {student_number:02d}",
                        "email": f"{username}@example.com",
                        "phone": f"031000000{student_number:02d}",
                        "user": user,
                        "school_class": school_class,
                        "age": 15,
                    },
                )

                students.append(student)

                student_number += 1

        self.stdout.write(
            self.style.SUCCESS("15 students ready.")
        )

        # -------------------------------------------------
        # 5. PARENTS
        # -------------------------------------------------

        parent_number = 1

        for student in students:

            username = f"demo_parent{parent_number:02d}"

            user, created = User.objects.get_or_create(
                username=username,
            )

            if created:
                user.set_password("Demo@12345")
                user.save()

            Parents.objects.get_or_create(
                user=user,
                defaults={
                    "student": student,
                },
            )

            parent_number += 1

        self.stdout.write(
            self.style.SUCCESS("15 parents ready.")
        )

        # -------------------------------------------------
        # 6. ATTENDANCE
        # -------------------------------------------------

        for student in students:

            Attendence.objects.get_or_create(
                student=student,
                status=True,
            )

        self.stdout.write(
            self.style.SUCCESS("Attendance records ready.")
        )

        # -------------------------------------------------
        # 7. MARKS
        # -------------------------------------------------

        for student in students:

            student_subjects = Subjects.objects.filter(
                school_class=student.school_class
            )

            for subject in student_subjects:

                Marks.objects.get_or_create(
                    student=student,
                    subject=subject,
                    exam_name="MID",
                    defaults={
                        "obtain_marks": 75,
                        "total_marks": 100,
                    },
                )

                Marks.objects.get_or_create(
                    student=student,
                    subject=subject,
                    exam_name="FINAL",
                    defaults={
                        "obtain_marks": 82,
                        "total_marks": 100,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS("Marks records ready.")
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Demo data created successfully!"
            )
        )