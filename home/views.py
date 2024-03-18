from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.views.decorators.csrf import csrf_exempt
import random
import string
from django.contrib import messages
# Create your views here.
from .serializer import *
def home(request):
    custom_id = request.COOKIES.get('custom_id')
    user_data = None
    if custom_id:
        try:
            user = User.objects.get(custom_id=custom_id)
            user_data = {
                'username': user.username,
                'email': user.email,
                # Add other user fields here if needed
            }
            print(user_data)
        except User.DoesNotExist:
            # Handle case where user with the given custom_id does not exist
            pass

    return render(request, 'home.html', {'user_data': user_data})

# def login_page(request):
#     return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')

# @csrf_exempt
def login_page(request):
    if request.method == 'POST':
        
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user=User.objects.filter(username=username).first()
            if user is None:
                return HttpResponse("User not found") 
            if not user.check_password(password):
                return HttpResponse("Incorrect Password")
            user_data = {
                'username': user.username,
                'email': user.email,
                    # Add other user fields here if needed
            }
            print(user_data)
            # return Response(user_data)
            if user is not None:
                # If user authentication is successful, redirect to some other page
                response = redirect('/')
                response.set_cookie(key='custom_id', value=user.custom_id, httponly=True)
                
                return response
                # return render(request, 'login.html', context=user_data)
                # return redirect('/', context=user_data)
            else:
                # If user authentication fails, render login template with error message
                return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    else:
        serializer = LoginSerializer()

    return render(request, 'login.html', {'serializer': serializer})



class LoginAPI(APIView):
    
    def post(self, request):
        try:
            data=request.data
            print(data)
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                print(serializer.data)
                username=serializer.data['username']
                password=serializer.data['password']
                
                user=User.objects.filter(username=username).first()
                print(user)
                if user is None:
                    return HttpResponse("User not found") 
                if not user.check_password(password):
                    return HttpResponse("Incorrect Password")
                user_data = {
                    'username': user.username,
                    'email': user.email,
                    # Add other user fields here if needed
                }
                return Response(user_data)
        except Exception as e:
            print(e)
            
            
class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data, status=201)  # Return created user data
            return Response(serializer.errors, status=400)  # Return validation errors
        except Exception as e:
            print(e)
    
    

# from .forms import UserForm

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/login/')
        else:
            messages.error(request, "Error occurred during registration.")
            return render(request,'register.html' )
    else:
        return render(request, 'register.html')
    # serializer = LoginSerializer(data=data)
    #         if serializer.is_valid():
    #             username=serializer.data['username']
    #             password=serializer.data['password']
                
    #             user=authenticate(email=username, password=password)
                
    #             if user is None:
    #                 return Response({
    #                 'status':404,
    #                 'message':'Invalid Password',
    #                 'data': {}
    #             })
                
    #             refresh = RefreshToken.for_user(user)

    #             return Response({
    #                 'refresh': str(refresh),
    #                 'access': str(refresh.access_token),
    #             })
                
    #         return Response({
    #             'status':400,
    #             'message':'Something went wrong',
    #             'data': serializer.errors
    #         })
    
    
def logout_page(request):
    # Delete the custom_id cookie to log the user out
    response = redirect('/')
    response.delete_cookie('custom_id')
    return response