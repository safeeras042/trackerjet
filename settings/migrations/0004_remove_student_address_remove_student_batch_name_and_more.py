# Generated by Django 4.2.1 on 2023-05-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_batch_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='batch_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]