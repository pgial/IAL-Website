from tabnanny import verbose
from django.db import models
from embed_video.fields import EmbedVideoField


class Module(models.Model):
    """
        Classe de módulo da disciplina de Introdução a Àlgebra Linear
    """
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000)
    number = models.IntegerField(primary_key=True)
    extra = models.BooleanField(default=False)

    def __str__(self):
        if self.extra:
            return self.title
        else:
            return '{} - {}'.format(str(self.number) ,self.title)

    class Meta:
        ordering = ['number']


class Topic(models.Model):
    """
        Classe de Tópico que pertence a um módulo
    """
    title = models.CharField(max_length=100, null=False, blank=False)
    fk_module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Module")
    order = models.IntegerField(default=0)
    extra = models.BooleanField(default=False, verbose_name='Extra module topic')

    def __str__(self):
        return 'Topic {}'.format(self.title)

    class Meta:
        ordering = ['order']

class Lesson(models.Model):
    """
        Classe de aula publicada
    """
    title = models.TextField(max_length=300)
    text = models.TextField(max_length=5000, blank=True, null=True)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fk_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return 'Lesson {}'.format(self.title)


class ExerciseList(models.Model):
    """
        Classe de lista de exercício (PDF)
    """
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True, null=True)
    pdf = models.FileField(upload_to='exercise_lists/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fk_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return 'Exercise List {}'.format(self.title)
