from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Student


class StudentListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = "student_add.html"
    success_url = reverse_lazy("student-list")
