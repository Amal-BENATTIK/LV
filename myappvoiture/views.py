from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from myappvoiture.models import *


def index(request):
    return render(request,'test.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def carsingle(request):
    return render(request,'carsingle.html')

def profil(request):
    return render(request,'Profil.html')
def orders(request):
    return render(request,'orders.html')
def register(request):
    return render(request,'Signup.html')



def list_voitures(request):
    voitures = Voiture1.objects.all()
    return render(request, 'test.html', {'voitures':voitures})


def Cars(request):
    voitures = Voiture1.objects.all()
    return render(request,'carlist.html',{'voitures':voitures})
def about(request):
    return render(request,'about.html')
def carlist(request):
    return render(request,'carlist.html')
def booking(request):
    return render(request,'booking.html')
def register(request):
    return render(request,'register.html')
def wishlist(request):
    return render(request,'wishlist.html')

class CarDetail(DetailView):
    model = Voiture1
    template_name = 'carsingle.html'
    context_object_name = 'car'


def logout_view(request):
    request.session['client_id']=None
    return redirect('/login')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        pn = request.POST['phone']
        client = Client1(Username=name,email=email, Pswd=password,Phone=pn,Language=None,HourFormat=None)
        client.save()
        return redirect('/login')
    else:
        return render(request, 'Signup.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            client = Client1.objects.get(email=email)
            if client.check_password(password):
                request.session['client_id'] = client.id
                context = {'Succes': ''}

                return redirect('i')
        except Client1.DoesNotExist:
            context = {'error': 'Invalid email or password'}
            return render(request, 'Login.html', context)
    return render(request, 'Login.html')

def add_reservation(request):
    client_id = request.session.get('client_id')
    if client_id is not None:
        client = Client1.objects.get(id=client_id)
        if request.method == 'POST':
            # Retrieve the form data from the request
            voiture_id = request.POST.get('voiture_id')
            client_id = request.POST.get('client_id')
            lieu_A = request.POST.get('PickupLocation')
            lieu_B = request.POST.get('DropoffLocation')
            dateA = request.POST.get('Pick Up Date')
            timeA = request.POST.get('Pick Up Time')
            dateB = request.POST.get('Collection Date')
            timeB = request.POST.get('Collection Time')

            # Create a new reservation object and save it to the database
            reservation = Reservation1(voiture_id=voiture_id, client_id=client_id, lieu_A=lieu_A, lieu_B=lieu_B,
                                       dateA=dateA, dateB=dateB)
            reservation.save()

            # Redirect to the reservation detail page or another appropriate page
            return redirect('car/' + voiture_id )
        else:
            # Render the form template for a GET request
            return render(request, 'test.html')

    else:
        return redirect('login')  # Replace 'login' with your desired URL


def client1_update(request, pk):
    client1 = get_object_or_404(Client1, pk=pk)

    if request.method == 'POST':
        client1.Username = request.POST.get('Username')
        client1.email = request.POST.get('email')
        client1.Pswd = make_password(request.POST.get('Pswd'))
        client1.Phone = request.POST.get('Phone')
        client1.Language = request.POST.get('Language')
        client1.HourFormat = request.POST.get('HourFormat')
        client1.save()
        print('succed')
        return redirect('update', pk=pk)

    return render(request, 'Profil.html', {'client1': client1})

