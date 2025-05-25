from django.urls import path
from .views import StudentListView

urlpatterns = [
    path("", StudentListView.as_view(template_name="student_list.html"),
         name="student-list"),
]
