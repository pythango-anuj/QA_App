# Generated by Django 4.2.7 on 2023-11-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_answer_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
