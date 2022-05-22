from django.contrib import admin

from .models import Module, Topic, Lesson, ExerciseList


admin.site.register(Module)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(ExerciseList)
