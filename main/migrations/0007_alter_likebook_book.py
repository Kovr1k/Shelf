# Generated by Django 5.0.2 on 2024-03-28 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_likebook_likeornot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likebook',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='main.book'),
        ),
    ]
