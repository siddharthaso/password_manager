from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user_profile.urls')),
    path('',include('password.urls')),
    path('',include('general.urls'))
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('debug/', include(debug_toolbar.urls)),
    ] + urlpatterns