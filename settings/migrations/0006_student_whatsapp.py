# Generated by Django 4.2.1 on 2023-05-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_student_district_student_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='whatsapp',
            field=models.TextField(max_length=20, null=True),
        ),
    ]