# Generated by Django 3.1.1 on 2020-10-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20201002_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]