# Generated by Django 4.0.3 on 2022-06-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_contact_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created',
        ),
    ]
