from django.contrib import admin
from django.urls import path, re_path

from pages.views import (
    api_placeholder,
    dashboard,
    event_detail,
    login_page,
    logout_page,
    notice_detail,
    notice_edit,
    shell_page,
)

urlpatterns = [
    path("", dashboard, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/login/", login_page, name="login"),
    path("accounts/logout/", logout_page, name="logout"),
    path("logout/", logout_page, name="logout_alt"),
    path("admin/", admin.site.urls),

    path("dashboard/monitoring/events/<int:event_id>/", event_detail, name="event_detail"),
    path("admin-panel/notices/<int:notice_id>/edit/", notice_edit, name="notice_edit"),
    path("admin-panel/notices/<int:notice_id>/", notice_detail, name="notice_detail"),

    # Lesson 01 skeleton API placeholder.
    path("api/auth/login/", api_placeholder, name="api_auth_login"),
    path("api/auth/me/", api_placeholder, name="api_auth_me"),
    re_path(r"^(api|dashboard/api|alerts/api)/.*$", api_placeholder, name="api_placeholder"),

    # Data-less page shells.
    re_path(r"^api/.*$", api_placeholder, name="api_placeholder"),
    re_path(r"^(?P<path>admin-panel/.*|dashboard/.*)$", shell_page, name="shell_page"),
]
