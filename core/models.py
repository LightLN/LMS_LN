from core.validators import phone_number_validator       # noqa

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


class BaseModel(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2)],
        db_column='first_name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2)],
        db_column='last_name'
    )
    phone_number = models.CharField(
        max_length=25,
        null=True,
        # validators=[phone_number_validator]
    )

    @classmethod
    def _generate(cls):
        fk = Faker()
        obj = cls(
            first_name=fk.first_name(),
            last_name=fk.last_name(),
            phone_number=fk.phone_number()
        )

        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        for _ in range(cnt):
            cls._generate()
