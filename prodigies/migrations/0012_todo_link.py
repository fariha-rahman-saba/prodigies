# Generated by Django 3.1.7 on 2021-04-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodigies', '0011_remove_todo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
