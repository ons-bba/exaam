from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Quiz, Question

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'

class QuestionCreateView(CreateView):
    model = Question
    fields = ['text']
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.quiz_id = self.kwargs['pk']
        return super().form_valid(form)

class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ['titre', 'nr_questions', 'etat']
    template_name = 'quiz_form.html'
    success_url = reverse_lazy('quiz_list')

def quiz_delete(request, pk):
    Quiz.objects.get(id=pk).delete()
    return redirect('quiz_list')

def question_list(request, quiz_id):
    questions = Question.objects.filter(quiz_id=quiz_id)
    return render(request, 'question_list.html', {'questions': questions})