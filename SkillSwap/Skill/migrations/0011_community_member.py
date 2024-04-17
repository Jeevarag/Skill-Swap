# Generated by Django 5.0.1 on 2024-03-15 04:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skill', '0010_delete_community'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='community_profile_pictures/')),
                ('is_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='led_communities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='Skill.community')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_communities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('community', 'member')},
            },
        ),
    ]