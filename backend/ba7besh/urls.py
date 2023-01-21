# # from django.urls import path
# # from django.conf.urls import include
# # from rest_framework import routers
# # from .views import *

# # router = routers.DefaultRouter()
# # router.register(r'restaurant', RestaurantViewSet)

# # urlpatterns = [

# #     path(r'^api/', include(router.urls)),
# #     path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# # ]

# from django.urls import path
# from .views import (RestaurantCreateAPI, RestaurantDetailAPI,
#                     ReviewCreateAPI, ReviewDetailAPI,
#                     BusinessInfoCreateAPI, BusinessInfoDetailAPI,
#                     BusinessCreateAPI, BusinessDetailAPI,
#                     ReviewLikeCreateAPI, ReviewLikeDetailAPI)

# urlpatterns = [
#     path('restaurant/', RestaurantCreateAPI.as_view(), name='restaurant-create'),
#     path('restaurant/<int:pk>', RestaurantDetailAPI.as_view(), name='restaurant-detail'),
#     path('review/', ReviewCreateAPI.as_view(), name='review-create'),
#     path('review/<int:pk>', ReviewDetailAPI.as_view(), name='review-detail'),
#     path('businessinfo/', BusinessInfoCreateAPI.as_view(), name='businessinfo-create'),
#     path('businessinfo/<int:pk>', BusinessInfoDetailAPI.as_view(), name='businessinfo-detail'),
#     path('business/', BusinessCreateAPI.as_view(), name='business-create'),
#     path('business/<int:pk>', BusinessDetailAPI.as_view(), name='business-detail'),
#     path('reviewlike/', ReviewLikeCreateAPI.as_view(), name='reviewlike-create'),
#     path('reviewlike/<int:pk>', ReviewLikeDetailAPI.as_view(), name='reviewlike-detail'),
# ]

from rest_framework import routers
from .views import RestaurantViewSet, ReviewViewSet, BusinessInfoViewSet, BusinessViewSet, ReviewLikeViewSet

router = routers.DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'businessinfo', BusinessInfoViewSet)
router.register(r'business', BusinessViewSet)
router.register(r'reviewlike', ReviewLikeViewSet)

urlpatterns = router.urls
