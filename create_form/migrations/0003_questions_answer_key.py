# Generated by Django 5.1.3 on 2024-11-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_form', '0002_auto_20241125_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answer_key',
            field=models.CharField(blank=True, default='Temporary', max_length=5000),
        ),
    ]
