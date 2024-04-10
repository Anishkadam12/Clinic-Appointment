
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('login', views.login),
    path('logout',views.logout),

    path('register1', views.register1, name='register1'),
    path('register2', views.register2, name='register2'),
    path('doctor_dash',views.doctor_dash, name='doctor_dash'),

    path('patient_log',views.patient_log),

    path('registration_form',views.registration_form, name='registration_form'),#1
    path('registration1',views.registration1, name='registration1'),            #2
    path('patient_dash',views.patient_dash),
    path('patient_logout',views.patient_logout),

    path('patient_appointment', views.patient_appointment, name='patient_appointment'),
    path('patient_app', views.patient_app, name='patient_app'),
    path('adminlog',views.adminlog),



    path('ref', views.ref_view, name='ref_view'),
    path('reffral',views.reffral, name='reffral'),

    path('pay', views.pay, name='pay'),
    path('payment',views.payment, name='payment'),
    path('medi',views.medi),

    path('approve', views.approve_view, name='approve_view'),
    path('report', views.report_view, name='report'),
    path('medicine', views.medicine_view, name='medicine'),
    path('delete/', views.delete_appointment, name='delete_appointment'),
    path('dashboard',views.dashboard),
    path('Doctor',views.Doctor_list),
    path('Patients',views.patients, name='Patients'),
    path('delete', views.delete_confirmation),
    path('cancel_appoint', views.cancel_appoint),
    path('inbox', views.inbox),
    path('hospital_doctor', views.hospital_doctor),









    # path('delete_appointment',views.cancel_appointment),





]

























    # path('register/', views.register_patient, name='register_patient'),
    # path('adminlog',views.adminlog),
    # path('dashboard',views.dashboard),
    # path('patient_dash',views.patient_dash),
    # path('ref/', views.ref_view, name='ref_view'),


