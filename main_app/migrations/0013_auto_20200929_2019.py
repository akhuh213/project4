# Generated by Django 3.1.1 on 2020-09-29 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200929_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
    ]
