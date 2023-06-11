# Generated by Django 4.2 on 2023-06-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0022_selection2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Selection',
        ),
        migrations.AddField(
            model_name='student',
            name='first_pay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_pay_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='second_pay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='second_pay_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='selection_type',
            field=models.CharField(choices=[('one_time', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='third_pay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='third_pay_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
