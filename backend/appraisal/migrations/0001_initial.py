# Generated by Django 4.0.4 on 2022-04-27 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('type', models.TextField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'epa_template',
            },
        ),
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('appraisee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appraisee', to=settings.AUTH_USER_MODEL)),
                ('appraiser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appraiser', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appraisal.template')),
            ],
            options={
                'db_table': 'epa_appraisal',
            },
        ),
    ]
