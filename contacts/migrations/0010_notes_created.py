# Generated by Django 4.0.3 on 2022-06-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_remove_notes_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
