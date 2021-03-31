# Generated by Django 3.1.7 on 2021-03-31 07:11

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.SlugField(max_length=32, unique=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('file', models.FileField(upload_to='videos/', verbose_name='Видео')),
            ],
        ),
    ]
