# Generated by Django 3.1.1 on 2021-01-15 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20210115_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmessage',
            name='duration',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]