# Generated by Django 5.1.3 on 2024-11-26 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_form', '0002_remove_form_background_color_remove_form_text_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='allow_view_score',
        ),
        migrations.RemoveField(
            model_name='form',
            name='is_quiz',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='score',
        ),
    ]
