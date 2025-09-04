from django.contrib import admin
from django.urls import path,include
from .views import ChatViewSet

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]




from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'chat', ChatViewSet)
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls