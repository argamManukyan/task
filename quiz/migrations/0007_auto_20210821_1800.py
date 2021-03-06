# Generated by Django 2.2.10 on 2021-08-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210821_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AlterModelOptions(
            name='quizitem',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='quizparticipation',
            options={'verbose_name': 'Ответ пользователя', 'verbose_name_plural': 'Ответы пользователей'},
        ),
        migrations.RemoveField(
            model_name='quizparticipation',
            name='id',
        ),
        migrations.AlterField(
            model_name='quizparticipation',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
