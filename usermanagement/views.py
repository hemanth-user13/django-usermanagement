from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("Received registration data:")
        print(request.data)  # Debugging: Print the raw request data

        if serializer.is_valid():
            # Debugging: Print the validated data
            print("Validated data:")
            print(serializer.validated_data)

            user = serializer.save()
            print("User registered successfully:")
            print(user)  # Debugging: Print the created user object
            
            return Response({
                'message': 'User registered successfully.',
                'user': serializer.data
            }, status=201)
        else:
            # Debugging: Print errors if the serializer is not valid
            print("Validation errors:")
            print(serializer.errors)
            return Response(serializer.errors, status=400)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        print("Login attempt:")
        print(f"Email: {email}")
        print(f"Password: {password}")

        user = CustomUser.objects.filter(email=email).first()
        
        if user and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            print("Login successful:")
            print("Access Token:", str(refresh.access_token))
            print("Refresh Token:", str(refresh))
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            print("Invalid credentials")
            return Response({'error': 'Invalid credentials'}, status=400)
