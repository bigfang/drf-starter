"""
URL configuration for drf-starter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from app.account import views as account_views


router = SimpleRouter(trailing_slash=False)
router.register('users', account_views.UserViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/profile', account_views.ProfileAPIView.as_view()),
    path('api/auth/login', account_views.LoginAPIView.as_view()),
    path('api/auth/logout', account_views.LogoutAPIView.as_view()),
    path('api/auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DJANGO_ENV == 'dev':
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns.extend([
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ])
