# Generated by Django 5.1.3 on 2024-11-26 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_form', '0003_questions_answer_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='answer_key',
        ),
    ]