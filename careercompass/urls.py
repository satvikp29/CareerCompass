from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("applications_list")),  # 👈 redirect root to /apps
    path("", include("tracker.urls")),
]
