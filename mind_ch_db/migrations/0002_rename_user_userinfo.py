# Generated by Django 5.0.3 on 2024-03-25 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mind_ch_db', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
    ]
