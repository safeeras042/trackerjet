# Generated by Django 4.2.1 on 2023-05-31 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_rename_course_name_course_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='course_name',
        ),
    ]
