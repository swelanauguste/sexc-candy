# Generated by Django 4.2.5 on 2023-10-23 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0009_letter_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='rec_from',
            new_name='_from',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='copied_to',
            new_name='copied',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='date_received',
            new_name='dated',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='sent_to',
            new_name='sent',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='date_on_doc',
        ),
        migrations.AddField(
            model_name='letter',
            name='received',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]