# Generated by Django 4.1.4 on 2022-12-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='untitled', max_length=80),
        ),
    ]
