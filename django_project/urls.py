from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # new
    path("apis/", include("apis.urls")), # new
    path("accounts/", include("django.contrib.auth.urls")), # new
    path("accounts/", include("accounts.urls")), # new
]
