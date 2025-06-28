from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("blog/", include("blog.urls", namespace="blog")),
]

# Только для режима разработки (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)