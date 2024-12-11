from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import person
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # type: ignore
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Use the name of the URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def login1(request):
    return render(request,'login1.html')

def home(request):
    return render(request,'homepage.html')

def sign(request):
    #records = {
    #    "fname":"Anhu",
    #    "lname":"NE"
    #}
    #'username' = request.POST['username']
        #'fname' = request.POST['fname']
        #'mname' = request.POST['mname']
        #'lname' = request.POST['lname']
        #'pwd' = request.POST['pwd']
    #person.insert_one(records)
    return render(request,'sign.html')
    #return HttpResponse("New person added")
def index(request):
    return HttpResponse("<h1>App is running...</h1>")

def show(request):
    persons = person.find()
    return persons

def message(request):
    return render(request,'Messages.html')