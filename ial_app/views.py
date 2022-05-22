from django.shortcuts import render
from django.http import HttpResponse

from .models import Module, Topic, Lesson, ExerciseList


def index(request):
    return render(request, 'index.html')

def modulo(request, module):
    requested_module = Module.objects.get(number=module)
    topics = Topic.objects.filter(fk_module=module)
    lessons = Lesson.objects.filter(fk_topic__in=topics)
    exercises = ExerciseList.objects.filter(fk_topic__in=topics)
    data = {
        'module': requested_module,
        'topics': topics,
        'lessons': lessons,
        'exercises': exercises
    }
    return render(request, 'modulo.html', data)
