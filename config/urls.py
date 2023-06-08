from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from apps.chat.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
