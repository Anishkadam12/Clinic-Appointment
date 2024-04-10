from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        em = request.POST.get('email')
        ps = request.POST.get('password')
        data = Doctor.objects.filter(email=em, password=ps)
        if data:
            messages.success(request, "Login Successfully Completed")
            return redirect("doctor_dash")
        else:
            messages.warning(request, "Login Failed....!")
            return render(request, 'login.html')
    else:

        return render(request, 'login.html')
def logout(request):
    # del request.session["username"]  #session end
    return redirect("/login")

def doctor_dash(request):
    data1 = Appointment.objects.all()
    data = Payment.objects.all()
    data2 = Referral.objects.all()
    return render(request, "doctor_dash.html", {'data1': data1, 'data': data, 'data2':data2})

def register1(request):
    return render(request,"register.html")

def register2(request):
    if request.method == 'POST':
        fn = request.POST['full_name']
        cn = request.POST['contact']
        sp = request.POST['specialization']
        em = request.POST['email']
        ps = request.POST['password']

        d = Doctor(full_name=fn, contact=cn, specialization=sp, email=em, password=ps)
        d.save()
        messages.success(request, 'Registration successfully!')

        return redirect("/login")
    else:
        return redirect("/register1")

def patient_log(request):
    if request.method == "POST":
        em = request.POST.get('email')
        ps = request.POST.get('password')
        data = Patient.objects.filter(email=em, password=ps)
        if data:
            messages.success(request, "Login Successfully Completed")
            return redirect("patient_appointment")
        else:
            messages.warning(request, "Login Failed....!")
            return render(request, 'patient_log.html')
    else:

        return render(request, 'patient_log.html')

def patient_dash(request):
    return render(request,'patient_dash.html')

def patient_logout(request):
    return render(request,'patient_log.html')

def registration_form(request):
    return render(request,'registration_form.html')

def registration1(request):
    if request.method == 'POST':
        fn = request.POST['full_name']
        cn = request.POST['contact']

        em = request.POST['email']
        ps = request.POST['password']

        p = Patient(full_name=fn, contact=cn, email=em, password=ps)
        p.save()
        messages.success(request, 'Registration successfully!')

        return redirect("/patient_log")
    else:
        return redirect("/registration_form")

def patient_appointment(request):
    return render(request,'patient_appointment.html')

def patient_app(request):
    if request.method == 'POST':
        pn = request.POST['patient_name']
        pa = request.POST['patient_age']
        ge = request.POST['gender']
        dn = request.POST['doctor_name']
        ad = request.POST['appointment_date']
        at = request.POST['appointment_time']
        rv = request.POST['reason_for_visit']
        ar = request.POST['address']
        cn = request.POST['contact']


        a = Appointment(patient_name=pn,patient_age=pa,gender=ge,doctor_name=dn,appointment_date=ad,appointment_time=at,reason_for_visit=rv,address=ar,contact=cn)
        a.save()
        messages.success(request, 'Appointment created successfully!')
        return redirect('/patient_dash')
    else:
            return redirect("/")

def adminlog(request):
    return render(request,'adminlog.html')

def ref_view(request):
    return render(request, 'ref.html')
def reffral(request):
    if request.method == 'POST':
        fn = request.POST['full_name']
        pn = request.POST['patient_name']
        r = request.POST['reason']
        b = Referral(full_name=fn,patient_name=pn,reason=r)
        b.save()
        messages.success(request, 'Referral submitted successfully!')
        return redirect('/patient_dash')
    else:
        return redirect("/")

def pay(request):
    return render(request,'pay.html')

def payment(request):
    if request.method == 'POST':
        n = request.POST['name']
        cn = request.POST['card_number']
        ed = request.POST['expiry_date']
        cv = request.POST['cvv']
        am = request.POST['amount']
        p = Payment(name=n,card_number=cn,expiry_date=ed,cvv=cv,amount=am)
        p.save()
        messages.success(request, 'Payment successfully Completed...!')
        return redirect('/patient_dash')
    else:
        return redirect("/")

def medi(request):
    return render(request,'medi.html')

def approve_view(request):
    return HttpResponse("Approve")

def report_view(request):
    # id = request.GET["id"]
    # data = Appointment.objects.all().filter(id=id)
    return render(request, "report.html")


def medicine_view(request):

    return render(request,'medi.html')


def delete_appointment(request):
    appointment_id = request.GET.get("id")

    if appointment_id:
        appointment = Appointment.objects.filter(id=appointment_id).first()
        if appointment:

            cancelled_appointment_info = CancelledAppointment.objects.create(
                appointment_id=appointment.id,
                patient_name=appointment.patient_name,

            )
            appointment.delete()
            messages.success(request, 'Appointment Cancelled Successfully...!')

            return redirect('/doctor_dash')
        else:

            return redirect('/cancel_appoint')


def dashboard(request):
    return render(request, "dashboard.html")

def Doctor_list(request):
    return render(request,'hospital-doctors-list.html')

def patients(request):
    data = Appointment.objects.all()
    return render(request,'hospital-patients.html',{'data': data})


def delete_confirmation(request):
    return render(request,'delete_confirmation.html')

def cancel_appoint(request):
    data1 = CancelledAppointment.objects.all()
    data = Appointment.objects.all()

    return render(request, 'cancel_appoint.html', {'data1': data1, 'data':data})

def inbox(request):
    data1 = CancelledAppointment.objects.all()
    return render(request,'inbox.html', {'data1': data1})

def hospital_doctor(request):
    data = Doctor.objects.all()
    return render(request, 'hospital-doctors.html',{'data': data})


































# def patient_log(request):
#     return render(request,"patient_log.html")
# def register_patient(request):
#     return render(request, 'registration_form.html')
#
# def adminlog(request):
#    return render(request,'adminlog.html')
#
# def dashboard(request):
#     return render(request,'dashboard.html')
# def ref_view(request):
#     # Your view logic here
#     return render(request, 'ref.html')
#
# def patient_dash(request):
#     return render(request,'patient_dash.html')

# def cancel_appointment(request):
#     data = CancelledAppointment.objects.all()
#     return render(request, 'cancel_appointment.html', {'data': data})






# def delete_appointment(request):
#     appointment_id = request.GET.get("id")
#
#     if appointment_id:
#         appointment = Appointment.objects.filter(id=appointment_id).first()
#         if appointment:
#             appointment.delete()
#             messages.success(request, 'Appointment Cancel Successfully...!')
#             return redirect('/doctor_dash')
#         else:
#             return redirect('/doctor_dash')



