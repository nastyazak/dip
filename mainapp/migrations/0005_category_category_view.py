# Generated by Django 4.2.1 on 2023-05-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_category_category_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_view',
            field=models.CharField(default='checkbox', max_length=100),
        ),
    ]
