# Generated by Django 4.2 on 2023-06-08 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0028_feedetails_remove_student_first_pay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedetails',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.student'),
        ),
    ]
