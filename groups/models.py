import datetime

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10)
    number_of_lessons = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name
