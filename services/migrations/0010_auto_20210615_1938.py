# Generated by Django 3.2 on 2021-06-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_visitask_visit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='amount',
        ),
        migrations.AlterField(
            model_name='visit',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]