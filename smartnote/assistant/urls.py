from rest_framework.routers import DefaultRouter
from .views import ToneViewSet, SummaryViewSet

router = DefaultRouter()
router.register(r'tones', ToneViewSet, basename='tone')
router.register(r'summaries', SummaryViewSet, basename='summary')

urlpatterns = router.urls