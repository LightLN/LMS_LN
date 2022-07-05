from django.db import models

from groups.models import Group

from teachers.validators import phone_number_validator


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, validators=[phone_number_validator])
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.speciality}, {self.phone_number}"
