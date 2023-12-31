# Generated by Django 4.2.5 on 2023-09-13 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0005_alter_letter_copied_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LetterComments',
            new_name='LetterComment',
        ),
        migrations.AlterField(
            model_name='letter',
            name='action',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='action_list', to='letters.action'),
        ),
    ]
