import datetime
import random

from core.models import BaseModel
from core.validators import adult_validator

from dateutil.relativedelta import relativedelta

from django.db import models

from faker import Faker

from groups.models import Group


class Student(BaseModel):

    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone_number}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        fkr = Faker()
        obj.birthday = fkr.date_between(start_date='-65y', end_date='-15y')
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()
