from rest_framework import routers

from .views import BusinessViewSet

router = routers.DefaultRouter()
router.register(r'business', BusinessViewSet)

urlpatterns = router.urls
