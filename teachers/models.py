from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.speciality}, {self.phone_number}"
