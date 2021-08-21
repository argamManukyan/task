from django.db.models import Value, IntegerField
from rest_framework import serializers, exceptions
from .models import Quiz, QuizItem, QuizParticipation, CustomUser


class QuizItemSerializer(serializers.ModelSerializer):
    """ Сериализатор вопроса """

    class Meta:
        model = QuizItem
        exclude = ['quiz']


class QuizSerializer(serializers.ModelSerializer):
    """ Сериализатор опроса """
    items = QuizItemSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"

    def create(self, validated_data):
        """ вырезание вопросов с помощю pop """
        items_data = validated_data.pop('items')
        quiz = Quiz.objects.create(**validated_data)

        for item in items_data:
            QuizItem.objects.create(quiz=quiz, **item)

        return quiz


class QuizUpdateAndDestroySerializer(serializers.ModelSerializer):
    """ Сериализатор опроса, который не дает админу изменить/удалить/добавить вопросы в опросе"""

    class Meta:
        model = Quiz
        fields = "__all__"


class QuizParticipationSerializer(serializers.ModelSerializer):
    """ Сериализатор для участие опроса """

    class Meta:
        model = QuizParticipation
        fields = ['quiz_item', 'user']

    def validate(self, attrs):
        quiz_items = attrs['quiz_item']
        current_quiz_id = set()
        for i in quiz_items:
            if current_quiz_id.__len__() > 1:
                raise exceptions.ValidationError({'detail': "Отправленные ответы не принадлежит одного вороса"})
            current_quiz_id.add(i.quiz.id)
        return attrs


class QuizUserSingleSerializer(serializers.ModelSerializer):
    """ Сериализатор для отоброжение ответы конкретного пользователя """
    results = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'results']

    def get_results(self, obj):
        quiz_list = []
        quiz_arr = QuizParticipation.objects.filter(user_id=obj.id).values('quiz_item__quiz__title',).distinct()
        for q in quiz_arr:
            item_dict = {
                'quiz_name': q['quiz_item__quiz__title'],
                'items': list(QuizParticipation.objects.filter(quiz_item__quiz__title=q['quiz_item__quiz__title']).values_list(
                    'quiz_item__text', flat=True).distinct())
            }
            quiz_list.append(item_dict)

        return quiz_list
