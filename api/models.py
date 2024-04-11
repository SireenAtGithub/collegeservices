from django.db import models
from django.core.validators import MinLengthValidator


class Semester(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING, default=None)


class Subject(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    code = models.CharField(
        max_length=10, unique=True, validators=[MinLengthValidator(5)]
    )
    semester = models.ForeignKey(
        Semester, on_delete=models.DO_NOTHING, related_name="subjects"
    )