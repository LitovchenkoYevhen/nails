# Generated by Django 3.2 on 2021-06-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_visitask_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitask',
            name='visit_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата визита'),
        ),
    ]