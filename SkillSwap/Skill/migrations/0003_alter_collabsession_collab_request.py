# Generated by Django 5.0.1 on 2024-02-12 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skill', '0002_collabrequest_collabsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collabsession',
            name='collab_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collab_sessions', to='Skill.collabrequest'),
        ),
    ]
