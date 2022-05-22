# Generated by Django 4.0.4 on 2022-05-17 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(db_column='f_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(db_column='l_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name'),
        ),
    ]
