from django.urls import path
from . views import PageViewSet, addText
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('page-views', PageViewSet)
router.register('telegram', addText)

urlpatterns = [
    # path('telegram/', addText.as_view(), name='text-telegram')
]

urlpatterns += router.urls