from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    '''
    Сериализатор для авторизации через Google
    '''
    email = serializers.EmailField()
    token = serializers.CharField()