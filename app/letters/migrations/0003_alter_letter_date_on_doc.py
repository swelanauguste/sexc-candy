# Generated by Django 4.2.5 on 2023-09-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_alter_letter_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='date_on_doc',
            field=models.DateField(verbose_name='date on document'),
        ),
    ]
