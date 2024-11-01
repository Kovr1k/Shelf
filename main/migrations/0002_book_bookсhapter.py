# Generated by Django 5.0.2 on 2024-03-05 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('dateOfPublication', models.DateField(blank=True, null=True, verbose_name='Дата публикации')),
                ('cover', models.ImageField(blank=True, upload_to='covers', verbose_name='Обложка')),
                ('description', models.TextField(default='', max_length=1000, verbose_name='Описание')),
                ('ageLimit', models.IntegerField(verbose_name='Возрастное ограничение')),
                ('published', models.BooleanField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookGenres', models.ManyToManyField(to='main.bookgenres')),
            ],
        ),
        migrations.CreateModel(
            name='BookСhapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('screensaver', models.ImageField(blank=True, upload_to='screensavers', verbose_name='Заставка')),
                ('number', models.IntegerField(blank=True, verbose_name='Номер главы в книге')),
                ('text', models.TextField(blank=True, verbose_name='Текст главы')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
    ]
