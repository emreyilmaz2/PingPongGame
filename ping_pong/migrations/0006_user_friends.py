# Generated by Django 4.1.4 on 2024-03-10 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping_pong', '0005_remove_friendlist_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='user_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
