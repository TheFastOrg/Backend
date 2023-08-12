from rest_framework import viewsets
from allauth.socialaccount.models import SocialAccount

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

        # Get the social account associated with the user
        social_account = get_social_account(request.user, 'google')

        # Get the user's uid and extra_data from the social account
        uid = social_account.uid
        extra_data = social_account.extra_data

        # Return the user token, uid, and extra_data in the response
        response_data = {
            'user_token': user_token,
            'uid': uid,
            'extra_data': extra_data
        }
        return Response(response_data)