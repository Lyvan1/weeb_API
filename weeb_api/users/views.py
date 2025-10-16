from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()