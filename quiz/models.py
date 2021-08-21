from django.core.exceptions import ValidationError
from django.db import models


class Quiz(models.Model):
    """ Модель опроса """
    title = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class QuizItem(models.Model):
    """ Модель вопроса . Можем и реализовать ManyToMany relation
        quiz = models.ManyToManyField(Quiz)
    """

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='items')
    ANSWER_TYPES = (
        ('text', "ответ текстом"),
        ('radio', "о одного варианта"),
        ('checkbox', "твет с выбором нескольких вариантов"),
    )
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPES)
    # Я здесь использую CharField , потому что в большеством случиях вопрос бывает коротким
    text = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.quiz} - {self.text[:10]}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.id}'


class QuizParticipation(models.Model):
    """ Модель для участие опроса """
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    quiz_item = models.ManyToManyField(QuizItem,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
