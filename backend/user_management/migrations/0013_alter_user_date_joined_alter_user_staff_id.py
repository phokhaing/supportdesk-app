# Generated by Django 4.0.4 on 2022-06-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0012_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default='2022-06-15 17:07:43'),
        ),
        migrations.AlterField(
            model_name='user',
            name='staff_id',
            field=models.CharField(default='0000', max_length=4, unique=True),
        ),
    ]
