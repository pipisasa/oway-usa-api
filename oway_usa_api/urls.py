from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from oway_usa_api.yasg import urlpatterns as doc_url

api_urls = [
    path("users/", include("apps.users.urls")),
    path("notifications/", include("apps.notifications.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]

urlpatterns += doc_url

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
