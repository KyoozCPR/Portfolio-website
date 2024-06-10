# Generated by Django 4.1.7 on 2024-05-27 14:28

import PollsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True, validators=[PollsApp.models.clean_email]),
        ),
    ]
