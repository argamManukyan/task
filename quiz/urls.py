from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import QuizAdminAPI, QuizUserAPI, QuizUserSingleAPI

router = SimpleRouter(trailing_slash=True)

router.register(r'quiz', QuizAdminAPI)

urlpatterns = [
    path('user-quiz/', QuizUserAPI.as_view(), name="user_quiz"),
    path('user/<id>/', QuizUserSingleAPI.as_view(), name='user_details')
] + router.urls
