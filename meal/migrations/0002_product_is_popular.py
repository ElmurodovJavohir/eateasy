# Generated by Django 4.2.7 on 2023-11-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]