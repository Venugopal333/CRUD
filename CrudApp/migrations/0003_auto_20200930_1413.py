# Generated by Django 3.1 on 2020-09-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0002_auto_20200930_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='No',
            field=models.IntegerField(unique=True),
        ),
    ]
