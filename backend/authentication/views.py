from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Token
from .serializers import TokenSerializer
from vendedores.models import Vendedores
from .utils import generate_token, check_password, hash_password
from ipdb import set_trace

class TokenView(APIView):
  def post(self, request):
    email=request.data['email']
    password = request.data['password']
    try:
      user = Vendedores.objects.get(email=email)
    except Vendedores.DoesNotExist:
      return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
      token = Token.objects.get(user=user)
    except Token.DoesNotExist:
      token = None
    if not token:
      token = generate_token()
      password = hash_password(password)
      token = Token.objects.create(user=user, token=token, password=password)
      return Response({'token': token.token, 'UID': user.id}, status=status.HTTP_201_CREATED)
    else:
      if not check_password(password, user):
        token.token = None
        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
      if check_password(password, user):
        token_hash = generate_token()
        token.token = token_hash
        token.save()
        return Response({'token': token.token, 'UID': user.id}, status=status.HTTP_200_OK)