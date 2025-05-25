from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    program = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"
