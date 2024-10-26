from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Admin  # Ensure this includes your Admin model
from .serializer import UserSerializer, AdminSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import AllowAny  # Import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any user
def signup(request):
    if request.method == 'POST':
        data = request.data.copy()  # Make a mutable copy of the request data
        if 'password' in data:
            data['password'] = make_password(data['password'])  # Hash the password
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(f'Signup successful for username: {data["username"]}')  # Debugging
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f'Signup failed: {serializer.errors}')  # Debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username').strip()
    password = request.data.get('password').strip()

    print(f'Attempting login with username: {username}, password: {password}')  # Debugging

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print('User does not exist')  # Debugging
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # Manually check the password
    is_correct = check_password(password, user.password)
    print(f'Password is correct: {is_correct}')  # Debugging

    if is_correct:
        return Response({'message': 'Login successful', 'email': user.email}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    username = request.data.get('username').strip()
    password = request.data.get('password').strip()

    print(f'Attempting admin login with username: {username}, password: {password}')  # Debugging

    try:
        admin = Admin.objects.get(username=username)
    except Admin.DoesNotExist:
        print('Admin does not exist')  # Debugging
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # Manually check the password
    is_correct = check_password(password, admin.password)
    print(f'Password is correct: {is_correct}')  # Debugging

    if is_correct:
        return Response({'message': 'Login successful', 'email': admin.email}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([AllowAny])  # Allow any user
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(f'Fetched {len(users)} users')  # Debugging
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])  # Allow any user
def clear_users(request):
    User.objects.all().delete()
    print('All users deleted')  # Debugging
    return Response({'message': 'Successfully deleted all users'}, status=200)