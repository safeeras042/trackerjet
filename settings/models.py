from django.db import models
from datetime import datetime

from django.contrib import admin


# Create your models here.
class State(models.Model):
    state_name=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.state_name
class District(models.Model):
    district_name=models.CharField(max_length=100,null=True,blank=True)
    state_name = models.ForeignKey(State,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.district_name

class Course(models.Model):
    course_name=models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.course_name

class Branch(models.Model):
    branch_name=models.CharField(max_length=100,blank=True,null=True)
    district_name=models.ForeignKey(District,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.branch_name


trainer_choice =(
    ('neethu','neethu'),
    ('gopika','Gopika')
)
    
class Batch(models.Model):
    course_name=models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    batch_name = models.CharField(max_length=20,null=True)
    trainer = models.CharField(max_length=6,null=True,choices=trainer_choice)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    def __str__(self):
        return self.batch_name



 
class CourseFees(models.Model):
    course = models.ForeignKey(Course,null=True, on_delete=models.CASCADE)
    fees_type = models.CharField(max_length=12,null=True, choices=(('one_time', 'One Time'), ('two_time', 'Two Time'), ('three_time', 'Three Time'),('registration','Registration')))
    amount = models.IntegerField(null=True)
    tax = models.DecimalField(max_digits=3,decimal_places=1,null=True)
    installment_period = models.IntegerField(null=True)

    def __str__(self):
        return self.fees_type
    



gender_choice = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER'),

)
yes_choice= (
    ('yes','Yes'),
    ('no','No'),
)
CHOICES = (
    ('one_times', 'One Time'),
    ('two_times', 'Two Times'),
    ('three_times', 'Three Times')
)

class Student(models.Model):

    name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=6,null=True,choices=gender_choice)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING,null=True)
    district = models.ForeignKey(District,on_delete=models.DO_NOTHING,null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    course = models.ForeignKey(Course,on_delete= models.DO_NOTHING,null=True)
    course_details = models.CharField(max_length=100, null=True, blank=True)
    batch = models.ForeignKey(Batch,null=True,on_delete=models.DO_NOTHING,blank=True)
    trainer = models.CharField(max_length=6,null=True,choices=trainer_choice)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    has_laptop = models.CharField(max_length=3, choices=yes_choice,blank=True)
    joining_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.name

 # Add 'name' and 'phone_number' to the list_display attribute



class FeesReceipt(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cheque', 'Cheque'),
    ]

    COLLECTED_TO_ACCOUNT_CHOICES = [
        ('oneteam ac 1', 'Oneteam ac 1'),
        ('oneteam ac 2', 'Oneteam ac 2'),
        ('oneteam ac 3', 'Oneteam ac 3'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=50)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_to_account = models.CharField(max_length=100, choices=COLLECTED_TO_ACCOUNT_CHOICES)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    description = models.TextField()
    receipt_image = models.ImageField(upload_to='receipts/')

    def __str__(self):
        return self.receipt_number


class FeeDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    selection_type = models.CharField(null=True,max_length=20, choices=CHOICES)
    first_pay = models.DateField(null=True, blank=True)
    first_pay_amount = models.IntegerField(null=True, blank=True)
    second_pay = models.DateField(null=True, blank=True)
    second_pay_amount = models.IntegerField(null=True, blank=True)
    third_pay = models.DateField(null=True, blank=True)
    third_pay_amount = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.selection_type == 'one_times':
            self.second_pay = None
            self.second_pay_amount = None
            self.third_pay = None
            self.third_pay_amount = None
        elif self.selection_type == 'two_times':
            self.third_pay = None
            self.third_pay_amount = None

        super().save(*args, **kwargs)

    
