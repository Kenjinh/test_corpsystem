import hashlib
import secrets
from django.conf import settings
from .models import Token
from ipdb import set_trace

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, user):
  password = hash_password(password)
  try:
    token = Token.objects.get(user=user)
  except Token.DoesNotExist:
    token = None
  if not token:
    return False
  return token.password.encode() == password.encode()
  

def generate_token():
  salt = secrets.token_bytes(16)
  key = settings.SECRET_KEY.encode()
  hashed_token = hashlib.pbkdf2_hmac('sha256', salt, key, 100000)
  return hashed_token.hex()