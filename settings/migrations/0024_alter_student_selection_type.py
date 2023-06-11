# Generated by Django 4.2 on 2023-06-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0023_delete_selection_student_first_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='selection_type',
            field=models.CharField(choices=[('one_times', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=20, null=True),
        ),
    ]