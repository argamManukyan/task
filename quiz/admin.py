from django.contrib import admin
from .models import Quiz, QuizItem, QuizParticipation

admin.site.register(Quiz)
admin.site.register(QuizItem)
admin.site.register(QuizParticipation)