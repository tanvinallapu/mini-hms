from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import SignupSerializer

User = get_user_model()


class SignupView(APIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def perform_create(self, serializer):

        user = serializer.save()

        try:

            requests.post(
                "http://localhost:3000/dev/send-email",
                json={
                    "type": "SIGNUP_WELCOME",
                    "email": user.email,
                    "username": user.username
                },
                timeout=10
            )

            print("WELCOME EMAIL TRIGGERED")

        except Exception as e:

            print("EMAIL ERROR")
            print(e)

    def post(self, request):

        serializer = SignupSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                'message': 'User created successfully'
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            token, created = Token.objects.get_or_create(
                user=user
            )

            return Response({
                'token': token.key,
                'role': user.role
            })

        return Response(
            {'message': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )