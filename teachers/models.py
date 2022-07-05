import random

from core.models import BaseModel

from django.db import models

from faker import Faker

from groups.models import Group


class Teacher(BaseModel):
    class Meta:
        db_table = 'teachers'

    speciality = models.CharField(max_length=50)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='teachers')

    def __str__(self):
        return f"{self.first_name}, {self.last_name} - {self.speciality}"

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        fkr = Faker()
        obj.speciality = fkr.job()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()
