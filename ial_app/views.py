from django.shortcuts import render
from django.http import HttpResponse

from .models import Module, Topic, Lesson, ExerciseList


def index(request):
    return render(request, 'index.html')

def modulo(request, module):
    requested_module = Module.objects.get(number=module)
    topics = Topic.objects.filter(fk_module=requested_module)
    lessons = Lesson.objects.filter(fk_topic__in=topics)
    exercises = ExerciseList.objects.filter(fk_topic__in=topics)
    data = {
        'module': requested_module,
        'topics': [
            parse_topic(topic, lessons, exercises, index) for index, topic in enumerate(topics)
        ]
    }
    return render(request, 'modulo.html', data)

def parse_topic(topic, lessons, exercises, index):
    return {
        'status': 'active' if index == 0 else '',
        'item': topic,
        'lessons': filter_lessons(topic, lessons),
        'exercises': filter_exercises(topic, exercises)
    }

def filter_lessons(topic, lessons):
    return [lesson for lesson in lessons if lesson.fk_topic.id == topic.id]

def filter_exercises(topic, exercises):
    return list(filter(lambda x: x.fk_topic.id == topic.id, exercises))

def about(request):
    return render(request, 'about.html')