from rest_framework import viewsets

from .models import Business
from .serializers import BusinessSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class GoogleLoginView(viewsets.ViewSet):
    def login(self, request):
        # Get the id_token from the request
        id_token = request.data.get('id_token')

        # Generate the user token using the id_token
        user_token = generate_user_token(id_token)

        # Get the user's email and name from the id_token
        email = get_email_from_id_token(id_token)
        name = get_name_from_id_token(id_token)

        # Return the user token, email, and name in the response
        response_data = {
            'user_token': user_token,
            'email': email,
            'name': name
        }
        return Response(response_data)