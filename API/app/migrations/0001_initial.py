# Generated by Django 4.2.1 on 2023-06-12 02:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.UUID('52501d17-1040-45cf-b7ae-922106a788e8'), editable=False, primary_key=True, serialize=False)),
                ('todo_title', models.CharField(max_length=25)),
                ('todo_description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
