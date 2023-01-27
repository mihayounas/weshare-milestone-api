# Generated by Django 3.2.16 on 2023-01-26 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blocked', '0006_auto_20230116_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='user',
        ),
        migrations.AddField(
            model_name='block',
            name='blocker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_blocker', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='blocked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blocked', to=settings.AUTH_USER_MODEL),
        ),
    ]
