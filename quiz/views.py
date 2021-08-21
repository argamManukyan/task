from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from .serializers import QuizSerializer, QuizUpdateAndDestroySerializer, QuizParticipationSerializer, \
    QuizUserSingleSerializer
from .models import Quiz, QuizItem, QuizParticipation, CustomUser


class QuizAdminAPI(ModelViewSet):
    """ API для администратора """
    queryset = Quiz.objects.all()
    lookup_field = 'pk'
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'create':
            return QuizSerializer
        return QuizUpdateAndDestroySerializer


class QuizUserAPI(generics.GenericAPIView):
    """ API для пользователей """
    queryset = Quiz.objects.filter(start_date__isnull=False, end_date__lte=datetime.now())

    def get_serializer_class(self):
        if self.request.method == "GET":
            return QuizUpdateAndDestroySerializer
        return QuizParticipationSerializer

    def get(self, request, *args, **kwargs):
        get_serializer = self.get_serializer_class()
        serializer = get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        CustomUser.objects.get_or_create(id=request.data['user'])
        get_serializer = self.get_serializer_class()
        serializer = get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizUserSingleAPI(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = QuizUserSingleSerializer
    lookup_field = 'id'


