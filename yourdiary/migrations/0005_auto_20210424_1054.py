# Generated by Django 3.1.4 on 2021-04-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourdiary', '0004_userparams_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userparams',
            name='avatar',
            field=models.ImageField(default='users_avatars/default_avatar.jpg', upload_to='users_avatars/'),
        ),
    ]