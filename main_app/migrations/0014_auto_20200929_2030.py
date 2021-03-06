# Generated by Django 3.1.1 on 2020-09-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20200929_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=5.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='zipcode',
            field=models.CharField(default=20152, max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.PositiveIntegerField(default=20152),
            preserve_default=False,
        ),
    ]
