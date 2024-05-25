from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.rooms.api import views

router = DefaultRouter()
router.register('', views.RoomViewSet, basename="room_api")

urlpatterns = [
    path('room/<int:pk>/', views.RoomUpdateDeleteRetrieveAPIView.as_view(), name='room'),
    path('', include(router.urls)),
]
urlpatterns += router.urls
