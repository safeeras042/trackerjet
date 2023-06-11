# Generated by Django 4.2 on 2023-06-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0027_remove_student_fees_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_type', models.CharField(choices=[('one_times', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=20, null=True)),
                ('first_pay', models.DateField(blank=True, null=True)),
                ('first_pay_amount', models.IntegerField(blank=True, null=True)),
                ('second_pay', models.DateField(blank=True, null=True)),
                ('second_pay_amount', models.IntegerField(blank=True, null=True)),
                ('third_pay', models.DateField(blank=True, null=True)),
                ('third_pay_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_pay',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_pay_amount',
        ),
        migrations.RemoveField(
            model_name='student',
            name='second_pay',
        ),
        migrations.RemoveField(
            model_name='student',
            name='second_pay_amount',
        ),
        migrations.RemoveField(
            model_name='student',
            name='selection_type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='third_pay',
        ),
        migrations.RemoveField(
            model_name='student',
            name='third_pay_amount',
        ),
    ]