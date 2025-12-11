from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.conf.urls import include
from api import views

router = DefaultRouter()
router.register('pieces', views.PieceViewSet)
router.register('media', views.MediaViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/pieces/titles', views.PieceViewSet.title_list),

    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]