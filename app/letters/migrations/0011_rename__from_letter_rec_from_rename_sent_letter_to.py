# Generated by Django 4.2.5 on 2023-10-23 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0010_rename_rec_from_letter__from_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='_from',
            new_name='rec_from',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='sent',
            new_name='to',
        ),
    ]