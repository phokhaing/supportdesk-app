# Generated by Django 4.0.4 on 2022-04-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0002_templatetype_alter_template_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TemplateType',
            new_name='Type',
        ),
    ]