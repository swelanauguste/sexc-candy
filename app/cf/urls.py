from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("letters.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

handler404 = "letters.views.my_custom_page_not_found_view"
# handler500 = 'mysite.views.my_custom_error_view'
# handler403 = 'mysite.views.my_custom_permission_denied_view'
# handler400 = 'mysite.views.my_custom_bad_request_view'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
