from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from .models import person_collection
from pymongo import MongoClient

# MongoDB connection
def sign(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # Insert data into MongoDB
        person_data = {
            'first_name': first_name,
            'username': username,
            'password': password  # NOTE: Hash passwords in production!
        }
        person_collection.insert_one(person_data)  # Save to MongoDB

        return HttpResponse("New person added successfully!")
    return render(request, 'login1.html')  # Render the sign-up page


# JSON-based API endpoint for handling JSON data
@csrf_exempt
def submit(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            print(f"Username: {username}, Password: {password}")
            return JsonResponse({
                "message": "Data received",
                "username": username,
                "password": password
            })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

# Login view (for traditional form-based login)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # type: ignore
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')  # Replace 'homepage' with your actual URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Renders the login page for users
def login1(request):
    return render(request, 'login1.html')

# Renders the home page
def home(request):
    return render(request, 'homepage.html')

def sign(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('fname')  # Matches the 'name' attribute in the form
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        
        # Save to the database (adjust according to your model)
        person.objects.create(
            username=username,
            first_name=first_name,
            password=password  # Note: Use hashing for passwords
        )
        return HttpResponse("New person added successfully!")
    
    return render(request, 'login1.html')

# Other static page rendering views
def message(request):
    return render(request, 'Messages.html')

def booking(request):
    return render(request, 'booking.html')

def blog(request):
    return render(request, 'blog.html')

def pack(request):
    return render(request, 'package.html')

def search(request):
    return render(request, 'search.html')

def hotel(request):
    return render(request,'hotels.html')

def flight(request):
    return render(request,'flight.html')

def train(request):
    return render(request,'trains.html')

def pay(request):
    return render(request,'payment.html')

def book(request):
    return render(request,'book.html')