(function () {
  const form = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");
  const serverError = document.getElementById("serverError");

  if (!form) return;

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const username = usernameInput ? usernameInput.value.trim() : "admin";
    const password = passwordInput ? passwordInput.value : "";

    if (!username) {
      if (serverError) {
        serverError.textContent = "아이디를 입력해주세요.";
        serverError.classList.add("show");
      }
      return;
    }

    if (password.length < 8) {
      if (serverError) {
        serverError.textContent = "비밀번호는 8자 이상 입력해주세요.";
        serverError.classList.add("show");
      }
      return;
    }

    localStorage.setItem("accessToken", "lesson01-demo-access-token");
    localStorage.setItem("refreshToken", "lesson01-demo-refresh-token");
    localStorage.setItem("username", username);
    localStorage.setItem("role", "admin");

    window.location.href = "/dashboard/";
  });
})();
