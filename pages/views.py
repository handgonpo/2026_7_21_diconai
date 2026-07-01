from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


MENU_TREE = [
    {
        "id": "safety",
        "label": "안전 확인",
        "icon": "shield",
        "children": [
            {"label": "나의 안전 확인", "path": "/dashboard/safety/checklist/"},
            {"label": "VR 교육", "path": "/dashboard/safety/vr/"},
            {"label": "안전 이력", "path": "/dashboard/safety/history/"},
        ],
    },
    {
        "id": "monitoring",
        "label": "모니터링",
        "icon": "monitor",
        "children": [
            {"label": "실시간 현황", "path": "/dashboard/monitoring/realtime/"},
            {"label": "작업자 현황", "path": "/dashboard/monitoring/workers/"},
            {"label": "이벤트 현황", "path": "/dashboard/monitoring/events/"},
            {"label": "유해가스 현황", "path": "/dashboard/monitoring/gas/"},
            {"label": "전력 시스템 현황", "path": "/dashboard/monitoring/power/"},
        ],
    },
    {
        "id": "settings",
        "label": "관리",
        "icon": "settings",
        "children": [
            {"label": "관리자 메뉴", "path": "/admin-panel/accounts-management/"},
            {"label": "내 정보", "path": "/dashboard/my-profile/"},
        ],
    },
]

DEMO_USER = {
    "id": 1,
    "username": "admin",
    "role": "super_admin",
    "is_staff": True,
    "is_superuser": True,
    "admin_url": "/admin-panel/accounts-management/",
    "menu_tree": MENU_TREE,
}

ALARM_TYPES = [
    {"value": "gas", "label": "유해가스"},
    {"value": "power", "label": "전력"},
    {"value": "worker", "label": "작업자"},
    {"value": "geofence", "label": "위험구역"},
]

EVENT_STATUSES = [
    {"value": "new", "label": "신규"},
    {"value": "in_progress", "label": "조치 중"},
    {"value": "resolved", "label": "조치 완료"},
]

ALERT_INTENSITIES = [
    {"value": "low", "label": "낮음"},
    {"value": "medium", "label": "보통"},
    {"value": "high", "label": "높음"},
    {"value": "critical", "label": "심각"},
]

SHELL_CONTEXT = {
    "is_demo": True,
    "departments": [],
    "facilities": [],
    "positions": [],
    "sensors": [],
    "alarm_types": ALARM_TYPES,
    "event_statuses": EVENT_STATUSES,
    "alert_intensities": ALERT_INTENSITIES,
    "current_user_display": "admin",
}

PAGE_TEMPLATES = {
    "dashboard/monitoring/realtime/": ("snb_details/monitoring_realtime.html", {}),
    "dashboard/monitoring/workers/": ("snb_details/monitoring_workers.html", {}),
    "dashboard/monitoring/events/": ("snb_details/monitoring_events.html", {}),
    "dashboard/monitoring/gas/": ("snb_details/monitoring_gas.html", {}),
    "dashboard/monitoring/power/": ("snb_details/monitoring_power.html", {}),
    "dashboard/safety/checklist/": ("snb_details/safety_checklist.html", {}),
    "dashboard/safety/vr/": ("snb_details/safety_vr.html", {}),
    "dashboard/safety/history/": ("snb_details/safety_history.html", {}),
    "dashboard/my-profile/": ("snb_details/my_profile.html", {}),
    "admin-panel/accounts-management/": ("admin_panel/accounts/accounts_main.html", {"active_nav": "account"}),
    "admin-panel/organizations/": ("admin_panel/organizations/organizations_main.html", {"active_nav": "org"}),
    "admin-panel/facility/": ("admin_panel/facility/facility.html", {"active_nav": "power_system"}),
    "admin-panel/power-system/": ("admin_panel/power_system/power_system.html", {"active_nav": "power_system"}),
    "admin-panel/gas-sensors/": ("admin_panel/gas_sensor/gas_sensor.html", {"active_nav": "gas_sensor"}),
    "admin-panel/geofence/": ("admin_panel/geofence/geofence_list.html", {"active_nav": "geofence"}),
    "admin-panel/map-editor/": ("admin_panel/map_editor/map_editor.html", {"active_nav": "map_editor"}),
    "admin-panel/data/gas/": ("admin_panel/data/gas_data.html", {"active_nav": "data"}),
    "admin-panel/data/power/": ("admin_panel/data/power_data.html", {"active_nav": "power_data"}),
    "admin-panel/data/retention-policy/": ("admin_panel/data/retention_policy.html", {"active_nav": "retention_policy"}),
    "admin-panel/logs/system/": ("admin_panel/logs/system_log.html", {"active_nav": "system_log"}),
    "admin-panel/logs/activity/": ("admin_panel/logs/activity_log.html", {"active_nav": "activity_log"}),
    "admin-panel/logs/integration/": ("admin_panel/logs/integration_log.html", {"active_nav": "integration_log"}),
    "admin-panel/logs/map-edit/": ("admin_panel/logs/map_edit_log.html", {"active_nav": "map_edit_log"}),
    "admin-panel/notices/": ("admin_panel/notices/notices_main.html", {"active_nav": "notice"}),
    "admin-panel/notices/create/": (
        "admin_panel/notices/notice_form.html",
        {"active_nav": "notice", "form_mode": "공지사항 등록", "form_mode_key": "create", "is_edit": False},
    ),
    "admin-panel/alerts/policies/": ("admin_panel/alerts/policies_main.html", {"active_nav": "alert_policy"}),
    "admin-panel/events/history/": ("admin_panel/events/event_history.html", {"active_nav": "event_history"}),
    "admin-panel/common-codes/": ("admin_panel/common_codes/common_codes.html", {"active_nav": "common_code"}),
    "admin-panel/thresholds/": ("admin_panel/thresholds/thresholds.html", {"active_nav": "threshold"}),
    "admin-panel/risk-standards/": ("admin_panel/risk_standards/risk_standards.html", {"active_nav": "risk_standard"}),
    "admin-panel/safety/checklist/": ("admin_panel/safety/checklist_main.html", {"active_nav": "policy"}),
    "admin-panel/safety/vr-training/": ("admin_panel/safety/vr_training_main.html", {"active_nav": "vr_training"}),
}


def login_page(request):
    if request.method == "POST":
        username = (
            request.POST.get("username")
            or request.POST.get("id")
            or request.POST.get("email")
            or "admin"
        )
        request.session["demo_username"] = username
        return redirect("/dashboard/")

    return render(request, "auth/login.html")


def dashboard(request):
    username = request.session.get("demo_username", "admin")

    context = {
        "username": username,
        "is_demo": True,
        "page_title": "산재 예방 통합 관제 시스템",
    }

    return render(request, "dashboard/main.html", context)


def shell_page(request, path=""):
    normalized_path = path.rstrip("/") + "/" if path else ""
    template_info = PAGE_TEMPLATES.get(normalized_path)
    if not template_info:
        return redirect("/dashboard/")

    template, extra_context = template_info
    context = {**SHELL_CONTEXT, **extra_context}
    return render(request, template, context)


def event_detail(request, event_id):
    return render(request, "snb_details/event_detail.html", {**SHELL_CONTEXT, "event_id": event_id})


def notice_detail(request, notice_id):
    return render(
        request,
        "admin_panel/notices/notice_detail.html",
        {**SHELL_CONTEXT, "active_nav": "notice", "notice_id": notice_id},
    )


def notice_edit(request, notice_id):
    return render(
        request,
        "admin_panel/notices/notice_form.html",
        {
            **SHELL_CONTEXT,
            "active_nav": "notice",
            "form_mode": "공지사항 수정",
            "form_mode_key": "edit",
            "is_edit": True,
            "notice_id": notice_id,
        },
    )


def logout_page(request):
    request.session.flush()
    return redirect("/accounts/login/")


@csrf_exempt
def api_placeholder(request, *args, **kwargs):
    path = request.path

    if path == "/api/auth/login/":
        return JsonResponse({
            "access": "lesson01-demo-access-token",
            "refresh": "lesson01-demo-refresh-token",
            "username": "admin",
            "role": "super_admin",
        })

    if path == "/api/auth/me/":
        return JsonResponse(DEMO_USER)

    if path == "/api/auth/profile/":
        return JsonResponse({
            **DEMO_USER,
            "name": "admin",
            "email": "admin@example.com",
            "department": "데모 부서",
            "position": "관리자",
        })

    if path == "/dashboard/api/refresh/":
        return JsonResponse({"ok": True, "admin_url": DEMO_USER["admin_url"]})

    if path == "/dashboard/api/safety-status/":
        return JsonResponse({"checklist_done": False, "vr_done": False})

    if path == "/dashboard/api/vr-content/active/":
        return JsonResponse({
            "id": 1,
            "title": "데모 VR 교육",
            "video_url": "/static/video/safety_vr.mp4",
            "duration": 0,
        })

    if path == "/dashboard/api/vr-progress/":
        return JsonResponse({"position": 0, "completed": False})

    if path == "/dashboard/api/workers-list/":
        return JsonResponse({"results": [], "workers": [], "count": 0})

    if path == "/api/safety/checklist/active/":
        return JsonResponse({
            "sections": [],
            "items": [],
            "message": "등록된 체크리스트가 없습니다.",
        })

    if path == "/alerts/api/alarms/summary/":
        return JsonResponse({"user_unread_event_count": 0, "count": 0})

    return JsonResponse({
        "results": [],
        "items": [],
        "data": [],
        "count": 0,
        "message": "Lesson 01 skeleton API placeholder",
    })
