# Generated by Django 3.1.1 on 2020-09-28 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200928_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
    ]
