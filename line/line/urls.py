"""line URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from users.views import ActivateAccount, SignUpView, BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', SignUpView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
