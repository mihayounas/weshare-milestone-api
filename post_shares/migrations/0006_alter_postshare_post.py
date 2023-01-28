# Generated by Django 3.2.16 on 2023-01-28 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_share'),
        ('post_shares', '0005_alter_postshare_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postshare',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_shares', to='posts.post'),
        ),
    ]