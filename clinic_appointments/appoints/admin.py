from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Referral)
admin.site.register(Payment)
admin.site.register(CancelledAppointment)


admin.site.register(Appointment)


