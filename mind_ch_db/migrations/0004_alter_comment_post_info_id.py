# Generated by Django 5.0.3 on 2024-03-28 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mind_ch_db', '0003_postinfo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Post_info_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mind_ch_db.postinfo'),
        ),
    ]
