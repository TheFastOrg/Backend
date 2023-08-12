from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def get_connect_redirect_url(self, request, socialaccount):
        print("hi")
        print(request)
        print(socialaccount)
        path = "/accounts/{username}/"
        return path.format(username=request.user.username)