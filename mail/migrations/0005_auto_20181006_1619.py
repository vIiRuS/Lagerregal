# Generated by Django 1.11.15 on 2018-10-06 14:19
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20181005_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='usage',
            field=models.CharField(blank=True, choices=[('lent', 'Device has been lent'), ('new', 'New Device is created'), ('reminder', 'Reminder that device is still owned'), ('returned', 'Device has been returned by user'), ('room', 'Room has been changed'), ('overdue', 'Reminder that device is overdue'), ('owner', 'Lending owner has been changed'), ('trashed', 'Device has been trashed')], max_length=200, null=True, verbose_name='Usage'),
        ),
    ]
