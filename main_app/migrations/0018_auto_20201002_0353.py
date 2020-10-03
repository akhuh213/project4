# Generated by Django 3.1.1 on 2020-10-02 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0017_auto_20201002_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.CharField(blank=True, choices=[('3M', '3m'), ('6M', '6m'), ('9M', '9m'), ('1y', '1yr'), ('2Y', '2yr'), ('3Y', '3yr'), ('4Y', '4yr'), ('5Y', '5yr')], max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('TY', 'Toys'), ('DP', 'Diapers'), ('CL', 'Clothes'), ('BK', 'Books'), ('OT', 'Others')], max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.CharField(blank=True, choices=[('NW', 'New'), ('LN', 'Like a new'), ('GD', 'Good'), ('FR', 'Fair')], max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]