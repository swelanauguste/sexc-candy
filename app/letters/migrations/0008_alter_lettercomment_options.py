# Generated by Django 4.2.5 on 2023-10-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0007_alter_lettercomment_options_letter_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lettercomment',
            options={'ordering': ['-created']},
        ),
    ]