# Generated by Django 3.2 on 2021-06-12 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_visitask_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitask',
            name='visit_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата визита'),
        ),
    ]