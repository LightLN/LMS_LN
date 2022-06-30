# Generated by Django 4.0.4 on 2022-06-30 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_remove_group_teacher'),
        ('students', '0005_remove_student_age_alter_student_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='groups.group'),
        ),
    ]