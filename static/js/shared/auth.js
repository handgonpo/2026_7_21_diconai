(function (window) {
  const DEMO_ACCESS = "lesson01-demo-access-token";
  const DEMO_REFRESH = "lesson01-demo-refresh-token";

  function ensureDemoTokens() {
    localStorage.setItem("accessToken", DEMO_ACCESS);
    localStorage.setItem("refreshToken", DEMO_REFRESH);
    localStorage.setItem("username", localStorage.getItem("username") || "admin");
    localStorage.setItem("role", localStorage.getItem("role") || "super_admin");
  }

  ensureDemoTokens();

  function jsonResponse(data, status = 200) {
    return Promise.resolve(
      new Response(JSON.stringify(data), {
        status: status,
        headers: { "Content-Type": "application/json" },
      })
    );
  }

  const DEMO_MENU_TREE = [
    {
      id: "safety",
      label: "안전 확인",
      icon: "shield",
      children: [
        { label: "나의 안전 확인", path: "/dashboard/safety/checklist/" },
        { label: "VR 교육", path: "/dashboard/safety/vr/" },
        { label: "안전 이력", path: "/dashboard/safety/history/" },
      ],
    },
    {
      id: "monitoring",
      label: "모니터링",
      icon: "monitor",
      children: [
        { label: "실시간 현황", path: "/dashboard/monitoring/realtime/" },
        { label: "작업자 현황", path: "/dashboard/monitoring/workers/" },
        { label: "이벤트 현황", path: "/dashboard/monitoring/events/" },
        { label: "유해가스 현황", path: "/dashboard/monitoring/gas/" },
        { label: "전력 시스템 현황", path: "/dashboard/monitoring/power/" },
      ],
    },
    {
      id: "settings",
      label: "관리",
      icon: "settings",
      children: [
        { label: "관리자 메뉴", path: "/admin-panel/accounts-management/" },
        { label: "내 정보", path: "/dashboard/my-profile/" },
      ],
    },
  ];

  const DEMO_USER = {
    id: 1,
    username: "admin",
    role: "super_admin",
    is_staff: true,
    is_superuser: true,
    admin_url: "/admin-panel/accounts-management/",
    menu_tree: DEMO_MENU_TREE,
  };

  window.Auth = {
    getAccessToken() {
      ensureDemoTokens();
      return DEMO_ACCESS;
    },

    getRefreshToken() {
      ensureDemoTokens();
      return DEMO_REFRESH;
    },

    setTokens(data) {
      localStorage.setItem("accessToken", data.access || DEMO_ACCESS);
      localStorage.setItem("refreshToken", data.refresh || DEMO_REFRESH);
      localStorage.setItem("username", data.username || "admin");
      localStorage.setItem("role", data.role || "super_admin");
    },

    clear() {
      // Lesson 01에서는 토큰 삭제하지 않음
      ensureDemoTokens();
    },

    getUsername() {
      ensureDemoTokens();
      return localStorage.getItem("username") || "admin";
    },

    getRole() {
      ensureDemoTokens();
      return localStorage.getItem("role") || "super_admin";
    },

    setRole(role) {
      localStorage.setItem("role", role || "super_admin");
    },

    isAuthenticated() {
      return true;
    },

    requireAuth() {
      ensureDemoTokens();
      return true;
    },

    logout() {
      window.location.href = "/accounts/login/";
    },

    redirectLogin() {
      window.location.href = "/accounts/login/";
    },

    async getMe() {
      ensureDemoTokens();
      return { ...DEMO_USER, username: this.getUsername(), role: this.getRole() };
    },

    apiFetch(url, options = {}) {
      ensureDemoTokens();

      if (typeof url === "string" && url.includes("/api/auth/me/")) {
        return jsonResponse({ ...DEMO_USER, username: this.getUsername(), role: this.getRole() });
      }

      if (typeof url === "string" && url.includes("/api/auth/profile/")) {
        return jsonResponse({
          ...DEMO_USER,
          username: this.getUsername(),
          role: this.getRole(),
          name: "admin",
          email: "admin@example.com",
          department: "데모 부서",
          position: "관리자",
        });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/refresh/")) {
        return jsonResponse({ ok: true, admin_url: DEMO_USER.admin_url });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/safety-status/")) {
        return jsonResponse({ checklist_done: false, vr_done: false });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/vr-content/active/")) {
        return jsonResponse({
          id: 1,
          title: "데모 VR 교육",
          video_url: "/static/video/safety_vr.mp4",
          duration: 0,
        });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/vr-progress/")) {
        return jsonResponse({ position: 0, completed: false });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/workers-list/")) {
        return jsonResponse({ results: [], workers: [], count: 0 });
      }

      if (typeof url === "string" && url.includes("/api/safety/checklist/active/")) {
        return jsonResponse({ sections: [], items: [], message: "등록된 체크리스트가 없습니다." });
      }

      if (typeof url === "string" && url.includes("/alerts/api/alarms/summary/")) {
        return jsonResponse({ user_unread_event_count: 0, count: 0 });
      }

      if (typeof url === "string" && url.includes("/alerts/api/")) {
        return jsonResponse({
          results: [],
          items: [],
          data: [],
          count: 0,
          message: "Lesson 01 skeleton alerts placeholder",
        });
      }

      if (typeof url === "string" && url.includes("/dashboard/api/")) {
        return jsonResponse({
          results: [],
          items: [],
          data: [],
          count: 0,
          message: "Lesson 01 skeleton dashboard placeholder",
        });
      }

      if (typeof url === "string" && url.startsWith("/api/")) {
        return jsonResponse({
          results: [],
          items: [],
          data: [],
          count: 0,
          message: "Lesson 01 skeleton API placeholder",
        });
      }

      return fetch(url, options);
    },
  };
})(window);
