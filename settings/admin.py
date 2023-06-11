from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django import forms
from .models import *
from django.urls import NoReverseMatch

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','course','fees_link')
    # fields = (('name','email'),('address','whatsapp'),('gender','state','district'),('course'))
    fieldsets = (
         ('Student Details',{'fields':(('name','email'),('address','whatsapp'),('gender','state','district'))

            }),
        ('Course Details',{'fields':('course','course_details','batch','trainer','start_date','end_date','has_laptop','joining_date')})

    )

    

    def fees_link(self, obj):
        try:
            url = f"/admin/settings/feedetails/?student__name={obj.name}"
            link = f'<a href="{url}">Go</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    fees_link.short_description = 'Fees'




    
class CourseFeesAdmin(admin.ModelAdmin):
    list_display = ('course', 'fees_type', 'amount','tax','display_installment_period',)

    fieldsets = (
        ('Fees Details', {
            'fields': ('course', 'fees_type', 'amount', 'tax', 'installment_period')
        }),
    )

    def display_installment_period(self, obj):
        return f"{obj.installment_period} months"

    display_installment_period.short_description = 'Installment Period'

# class FeesAdmin(admin.ModelAdmin):
#     list_display = ('student', 'payment_date', 'paid_amount', 'balance_amount', 'payment_link')


#     def payment_link(self, obj):
#         url = reverse('admin:settings_feesreceipt_add')  # Replace <app_name> with your app name
#         link = f'<a href="{url}?student_id={obj.student.id}">Pay</a>'
#         return format_html(link)

#     payment_link.short_description = 'Payment'
#     payment_link.allow_tags = True

#     list_display_links = ('payment_link',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Fees details of {}'.format(FeesReceipt._meta.get_field('student').verbose_name.capitalize())
        return super().changelist_view(request, extra_context=extra_context)



class FeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('student','first_pay', 'first_pay_amount','payment','second_pay','second_pay_amount','payment','third_pay','third_pay_amount','payment')
    list_filter = ('student__name',)

    def payment(self, obj):
        url = reverse('admin:settings_feesreceipt_add') 
        link = f'<a href="{url}?student_id={obj.student_id}">Pay</a>'
        return format_html(link)

    payment.short_description = 'Payment'

class FeesReceiptAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'paid_amount', 'receipt_number', 'payment_mode', 'description', 'collected_to_account')

admin.site.register(State)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Batch)
admin.site.register(Course)
admin.site.register(Student,StudentAdmin)
admin.site.register(CourseFees, CourseFeesAdmin)
admin.site.register(FeesReceipt,FeesReceiptAdmin)
admin.site.register(FeeDetails,FeeDetailsAdmin)

