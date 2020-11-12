# Generated by Django 3.1.2 on 2020-10-23 11:33

from django.db import migrations, models
import note.note_enums


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='enums',
            field=models.CharField(choices=[(note.note_enums.NoteStatusChoice['published'], 'published'), (note.note_enums.NoteStatusChoice['draft'], 'draft'), (note.note_enums.NoteStatusChoice['deleted'], 'deleted')], max_length=20),
        ),
    ]
