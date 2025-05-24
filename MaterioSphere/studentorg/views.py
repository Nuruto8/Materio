# studentorg/views.py
from django.shortcuts import render


def student_list(request):
    # your logic here
    return render(request, 'studentorg/student_list.html')
