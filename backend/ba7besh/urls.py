from rest_framework import routers
from .views import RestaurantViewSet, ReviewViewSet, BusinessInfoViewSet, BusinessViewSet, ReviewLikeViewSet

router = routers.DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'businessinfo', BusinessInfoViewSet)
router.register(r'business', BusinessViewSet)
router.register(r'reviewlike', ReviewLikeViewSet)

urlpatterns = router.urls
