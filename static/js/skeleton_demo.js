(function () {
  console.log("[Lesson 01 Skeleton] demo mode enabled");

  // 기존 프론트가 로그인 토큰을 찾는 경우를 대비해서 임시 토큰 저장
  localStorage.setItem("accessToken", "lesson01-demo-token");
  localStorage.setItem("refreshToken", "lesson01-demo-refresh-token");
  localStorage.setItem("username", "admin");
  localStorage.setItem("role", "admin");

  // 로그인 폼은 실제 API 호출 대신 dashboard로 이동
  document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        window.location.href = "/dashboard/";
      });
    });

    const loginButtons = document.querySelectorAll("button");

    loginButtons.forEach(function (button) {
      const text = button.innerText || button.textContent || "";

      if (text.includes("로그인")) {
        button.addEventListener("click", function (event) {
          event.preventDefault();
          window.location.href = "/dashboard/";
        });
      }
    });
  });
})();
