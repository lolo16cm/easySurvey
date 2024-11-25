# Generated by Django 5.1.2 on 2024-11-24 10:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=5000)),
                ('is_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=10000)),
                ('question_type', models.CharField(max_length=20)),
                ('required', models.BooleanField(default=False)),
                ('answer_key', models.CharField(blank=True, max_length=5000)),
                ('score', models.IntegerField(blank=True, default=0)),
                ('feedback', models.CharField(max_length=5000, null=True)),
                ('choices', models.ManyToManyField(related_name='choices', to='create_form.choices')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('background_color', models.CharField(default='#d9efed', max_length=20)),
                ('text_color', models.CharField(default='#272124', max_length=20)),
                ('collect_email', models.BooleanField(default=False)),
                ('authenticated_responder', models.BooleanField(default=False)),
                ('edit_after_submit', models.BooleanField(default=False)),
                ('confirmation_message', models.CharField(default='Your response has been recorded.', max_length=10000)),
                ('is_quiz', models.BooleanField(default=False)),
                ('allow_view_score', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(related_name='questions', to='create_form.questions')),
            ],
        ),
    ]