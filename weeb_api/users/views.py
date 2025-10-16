from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    __ViewSet to handle Users__
    Define automatically:
        GET (/users) --> list()
        GET (/users/{id}) --> retrieve()
        POST (/users) --> create()
        PUT (/users/{id}) --> update()
        PATCH (/users/{id}) --> partiel_update()
        DELETE (/users/{id} --> destroy()
    """
    queryset = User.objects.all()
    #serializer_class = UserSerializer
    
    # Route /users | Method GET
    def list(self, request, *args, **kwargs):
        print(self.queryset)
        return Response(self.queryset.values('id', 'first_name', 'last_name', 'email'))