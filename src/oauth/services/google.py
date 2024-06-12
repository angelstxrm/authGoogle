from src.oauth import serializers
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed



def check_google_auth(google_user: serializers.GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request())
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Invalid token')
    
    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    