# Generated by Django 4.0.4 on 2022-04-27 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appraisal', '0008_alter_appraisal_appraisee_alter_appraisal_appraiser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisal',
            name='updated_by',
            field=models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]