# Generated by Django 4.2.5 on 2023-11-14 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_status_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('-expires',), 'verbose_name_plural': 'statuses'},
        ),
    ]