from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

from .api import router

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/", include(router.urls)),
        path("auth/", include("apps.authentication.urls"), name="authentication"),
    ]
    + staticfiles_urlpatterns()
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
