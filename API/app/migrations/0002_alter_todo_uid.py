# Generated by Django 4.2.1 on 2023-06-12 03:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('585b0990-4e50-40ac-9b6c-1e2971eda2ec'), editable=False, primary_key=True, serialize=False),
        ),
    ]
