# Generated by Django 3.2.25 on 2024-03-07 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ping_pong', '0003_user_has_logged_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Beklemede'), ('accepted', 'Kabul Edildi'), ('rejected', 'Reddedildi')], default='pending', max_length=20)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_friend_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_friend_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
