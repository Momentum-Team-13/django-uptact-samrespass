# Generated by Django 4.0.3 on 2022-06-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_notes_created_alter_contact_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.notes'),
        ),
    ]