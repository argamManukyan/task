# Generated by Django 2.2.10 on 2021-08-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20210821_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizparticipation',
            name='user_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
