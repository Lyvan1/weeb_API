from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet to handle contact submissions."""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'success': True,
            'message': 'Contact saved successfully.',
            'results': serializer.data
        }, status=status.HTTP_201_CREATED)


