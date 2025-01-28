from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, world!")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered!')
        else:
            UserDetails.objects.create(username=username, email=email, password=password)
            messages.success(request, 'Signup successful! Please log in.')
            return redirect('login')

    return render(request, 'Loginify/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('success')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password!')

    return render(request, 'Loginify/login.html')

def success(request):
    return render(request, 'Loginify/success.html')

def get_all_users(request):
    users = UserDetails.objects.all().values()
    return JsonResponse(list(users), safe=False)

def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return JsonResponse({'username': user.username, 'email': user.email, 'password': user.password})
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@csrf_exempt
def update_user_password(request, email, new_password):
    if request.method == 'POST':
        try:
            # Find the user by email
            user = UserDetails.objects.get(email=email)

            # Update the password
            user.password = new_password
            user.save()

            # Return success response
            return JsonResponse({'message': 'Password updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

