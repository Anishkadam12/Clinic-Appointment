from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)



class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    DOCTOR_CHOICES = [
        ('Dr. Sandip Bhirud', 'Dr. Sandip Bhirud (Dentist)10.00AM To 2:00PM'),
        ('Dr. Kishore Jadhavar', 'Dr. Kishore Jadhavar (Psychiatrist)10.00AM To 2:00PM'),
        ('Dr. Priya Palimkar', 'Dr. Priya Palimkar (Cardiology)10.00AM To 2:00PM'),
        ('Dr. Pratik Patil', 'Dr. Pratik Patil (Oncologist)10.00AM To 2:00PM'),
        ('Dr. Mahesh Sabade', 'Dr. Mahesh Sabade (Ayurveda)10.00AM To 2:00PM'),
        ('Dr. Atul Patil', 'Dr. Atul Patil (General surgeon)10.00AM To 2:00PM'),
    ]

    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    doctor_name = models.CharField(max_length=100, choices=DOCTOR_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason_for_visit = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)

class Referral(models.Model):
    full_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)

class Payment(models.Model):
    name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class CancelledAppointment(models.Model):
    appointment_id = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"Cancelled Appointment ID: {self.appointment_id}, Patient: {self.patient_name}"








