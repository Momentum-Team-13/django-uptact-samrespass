# Generated by Django 4.0.3 on 2022-06-28 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_alter_contact_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='notes',
            new_name='note',
        ),
    ]