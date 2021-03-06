# Generated by Django 3.2.13 on 2022-05-22 12:39

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('extra', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('extra', models.BooleanField(default=False)),
                ('fk_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ial_app.module')),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('text', models.TextField(blank=True, max_length=5000, null=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('fk_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ial_app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('pdf', models.FileField(upload_to='exercise_lists/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('fk_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ial_app.topic')),
            ],
        ),
    ]
