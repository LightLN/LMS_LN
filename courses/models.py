from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='name',
        validators=[MinLengthValidator(2)]
    )
    educational_direction = models.CharField(
        max_length=40,
        verbose_name='educational direction',
        validators=[MinLengthValidator(3)]
    )
    count_disciplines = models.IntegerField(
        verbose_name='count disciplines',
        validators=[MinValueValidator(5), MaxValueValidator(20)]
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name
