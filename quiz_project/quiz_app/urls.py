from django.urls import path
from .views import QuizListView, QuestionCreateView, QuizUpdateView, quiz_delete, question_list

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', quiz_delete, name='quiz_delete'),
    path('quiz/<int:pk>/questions/', question_list, name='question_list'),
    path('quiz/<int:pk>/add_question/', QuestionCreateView.as_view(), name='add_question'),
]