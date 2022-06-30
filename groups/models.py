import datetime

from django.db import models

from teachers.models import Teacher


class Group(models.Model):
    name = models.CharField(max_length=10)
    number_of_lessons = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.name} {self.number_of_lessons}'
