# Generated by Django 4.0.4 on 2022-07-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatars/'),
        ),
    ]
