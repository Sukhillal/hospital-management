from django.contrib import admin
from . models import Dep,Doctors,Booking

# Register your models here.

admin.site.register(Dep)

admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=("id","p_name","p_phone","p_email","doc_name","booking_date","booking_on")

admin.site.register(Booking,BookingAdmin)


