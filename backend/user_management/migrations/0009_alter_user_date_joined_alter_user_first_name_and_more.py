# Generated by Django 4.0.4 on 2022-06-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_alter_user_date_joined_alter_user_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default='2022-06-15 16:46:40'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]