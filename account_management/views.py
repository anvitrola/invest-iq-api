from django.conf import settings

# Create your views here.
from django.contrib.auth import password_validation
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from account_management.serializers import AccountRegistrationSerializer, AccountSerializer


class CreateAccount(APIView):
    permission_classes = (AllowAny, )
    serializer_class = AccountRegistrationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        # Validate password
        try:
            password_validation.validate_password(data['password'])
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'message': 'Account created successfully'}, status=HTTP_201_CREATED)
    
class GetAccount(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user  # The authenticated user is available in the request

        # You can return the user data as needed
        return Response({'email': user.email, 'full_name': user.full_name}, status=HTTP_200_OK)
  
class UpdateAccount(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=HTTP_200_OK)
 

