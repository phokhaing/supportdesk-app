# Generated by Django 4.0.4 on 2022-06-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0011_remove_user_is_supperuser_alter_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default='2022-06-15 16:51:54'),
        ),
    ]
