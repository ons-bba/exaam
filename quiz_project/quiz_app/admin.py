from django.contrib import admin
from .models import Quiz, Formateur, Question

class QuizAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nr_questions', 'etat')
    search_fields = ('titre',)
    list_filter = ('etat',)
    actions = ['set_disponible']

    def set_disponible(self, request, queryset):
        queryset.update(etat='dispo')
    set_disponible.short_description = "Réinitialiser à 'Disponible'"

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Formateur)
admin.site.register(Question)