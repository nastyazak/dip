# Generated by Django 4.2.1 on 2023-06-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_typework_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='typework',
            name='hours',
            field=models.IntegerField(default=1),
        ),
    ]