# Generated by Django 4.2.1 on 2023-06-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=55)),
                ('author_name', models.CharField(max_length=55)),
                ('published_date', models.CharField(max_length=55)),
                ('book_price', models.IntegerField()),
            ],
        ),
    ]
