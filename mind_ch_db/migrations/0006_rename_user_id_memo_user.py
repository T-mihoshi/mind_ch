# Generated by Django 5.0.3 on 2024-03-28 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mind_ch_db', '0005_memo_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='user_id',
            new_name='user',
        ),
    ]
