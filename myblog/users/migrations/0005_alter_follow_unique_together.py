# Generated by Django 5.1.1 on 2024-10-08 22:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_member_profile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
    ]
