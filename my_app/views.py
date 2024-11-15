from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .models import Students
from .models import Contact
from .forms import Studentsform
from .forms import ContactForm


# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'main.html')
    
    def post(Self, request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        address=request.POST.get('address')
        
        if name and email and number and address :
            Contact.objects.create(name=name, email=email, number=number, address=address)
        obj=Contact.objects.all()
        
        return render(request, 'data2.html', {'objs':obj})  
        

class DataView2(View):
    def get(self, request):
        obj=Contact.objects.all()
        return render(request, 'data2.html', {'objs':obj})

class IndexView(View):
    def get(self, request):
        form= SignUpForm()
        return render(request, 'signup.html', {'form':form})
    def post(self, request):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')
        return render(request, 'signup.html', {'form':form})

class AddData(View):
    def get(self, request):
        form=AuthenticationForm()
        return render(request,'signin.html', {'form':form})
    
    def post(self, request):
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home2')
        return render(request, 'signin.html', {'form':form})
    
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return redirect('/signin')
        
    def post(self,request):
        user_id=request.POST.get('user_id')
        client_name=request.POST.get('client_name')
        areas_of_working=request.POST.get('areas_of_working')
        work_date=request.POST.get('work_date')
        claim_id=request.POST.get('claim_id')
        insurance=request.POST.get('insurance')
        patient=request.POST.get('patient')
        billed_amount=request.POST.get('billed_amount')
        service_data=request.POST.get('service_data')
        balance=request.POST.get('balance')
        status=request.POST.get('status')
        reason=request.POST.get('reason')
        action=request.POST.get('action')
        payment_information=request.POST.get('payment_information')
        patient_responsibility=request.POST.get('patient_responsibility')
        cheque_no=request.POST.get('cheque_no')
        cheque_date=request.POST.get('cheque_date')
        paid_status=request.POST.get('paid_status')
        paid_by=request.POST.get('paid_by')
        denial_code=request.POST.get('denial_code')
        add_corrected=request.POST.get('add_corrected')
        dx_corrected=request.POST.get('dx_corrected')
        cpt=request.POST.get('cpt')
        solutions=request.POST.get('solutions')
        if user_id and client_name and areas_of_working and work_date and claim_id and insurance and patient and service_data and balance and status and reason and action and payment_information and patient_responsibility and cheque_no and cheque_date and paid_status and paid_by and denial_code and add_corrected  and dx_corrected and cpt and solutions and billed_amount:

            Students.objects.create(user_id=user_id, client_name=client_name, areas_of_working=areas_of_working, work_date=work_date, claim_id=claim_id, insurance=insurance, patient=patient, service_data=service_data, balance=balance, status=status, reason=reason, action=action, payment_information=payment_information, patient_responsibility=patient_responsibility, cheque_no=cheque_no, cheque_date=cheque_date, paid_status=paid_status, paid_by=paid_by, denial_code=denial_code, add_corrected=add_corrected, dx_corrected=dx_corrected, cpt=cpt, solutions=solutions, billed_amount=billed_amount )
        form  =   Studentsform(request.POST)
        if form.is_valid():
            form.save()

            context =  {'msg':'*Report send  sucessfully to staya '}
            return render(request, 'home.html', context)
        else:
            context =  {'error':form}
            return render(request, 'home.html', context)
        

    
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/signin')

from datetime import datetime
import pandas as pd
from django.http import HttpResponse
from django.db.models import Q
class DataView(View):
    def get(self, request):
        search = request.GET.get('search')
        date = request.GET.get('date')
        print(date)
        
        # Default query: All students
        obj = Students.objects.all()
        
        # If 'search' is provided, filter by client_name
        if search:
            obj = obj.filter(Q(client_name__icontains=search)| Q(client_name__contains=search) )
        
        # If 'date' is provided, filter by start_date (ensure proper date format)
        if date:
            # Assuming the 'date' format is 'YYYY-MM-DD'
            date_object = datetime.strptime(date, '%Y-%m-%d').date()
            obj = obj.filter(start_date__date=date_object)
            data = list(obj.values(
        'id', 'client_name',  'areas_of_working', 'claim_id', 
        'insurance', 'patient', 'service_data', 'balance', 'status', 
        'reason', 'action', 'payment_information', 'patient_responsibility', 
        'cheque_no',  'paid_status', 'paid_by', 'denial_code', 
        'add_corrected', 'dx_corrected', 'cpt', 'solutions', 'billed_amount'
    ))

            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data)

            # If the date filtering is applied, format the 'start_date' and 'cheque_date' as strings (optional)
            if 'start_date' in df.columns:
                # df['start_date'] = pd.to_datetime(df['start_date']).dt.strftime('%Y-%m-%d')
                pass
            if 'cheque_date' in df.columns:
                # df['cheque_date'] = pd.to_datetime(df['cheque_date']).dt.strftime('%Y-%m-%d')
                pass


            # Create an HTTP response with the appropriate Excel file content type
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=students_data.xlsx'

            # Write the DataFrame to the Excel file and save it in the response object
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Students')

            return response
        return render(request, 'data.html', {'objs': obj})

    
class HomeView2(View):
    def get(self , request):
        search = request.GET.get('search')
        print('search',search )
        if search:
            obj = Students.objects.filter(Q(client_name__icontains=search)| Q(client_name__contains=search))
        else:
            obj=Students.objects.all()
        print('obj', obj)
        context={'objs':obj}
        return render(request, 'home2.html', context)
    
        


class LearnView(View):
    def get(self , request):
        return render(request, 'learn.html')