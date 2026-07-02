# diconai-remake

산재 예방 통합 관제 플랫폼을 Django 기초부터 다시 구현하기 위한 수업용 skeleton 프로젝트입니다.

## Lesson 01 목표

- 기존 프로젝트의 HTML, CSS, JavaScript 화면만 유지
- Docker, FastAPI, K8s, Celery, Redis, PostgreSQL, AI 모델 제거
- Django 기본 구조에서 accounts/login, dashboard 화면 렌더링
- 이후 수업 단계에서 models.py, views.py, API, WebSocket, AI 기능을 다시 구현

## 소스 내려받기 및 실행 방법
이 프로젝트는 GitHub의 `2026_7_21_source` 브랜치를 기준으로 내려받아 실행한다.

---

### 1. 작업 폴더로 이동

```bash
cd ~/2026_6-17_diconai
```

---

### 2. 소스 클론

```bash
git clone -b 2026_7_21_source --single-branch https://github.com/handgonpo/2026_7_21_diconai.git 2026_7_21_source
```

위 명령어는 GitHub 저장소에서 `2026_7_21_source` 브랜치만 내려받아  
내 컴퓨터에 `2026_7_21_source` 폴더로 저장한다.

---

### 3. 프로젝트 폴더로 이동

```bash
cd 2026_7_21_source
```

현재 브랜치를 확인한다.

```bash
git branch
```

정상이라면 다음처럼 표시된다.

```text
* 2026_7_21_source
```

---

### 4. 가상환경 생성

```bash
uv venv
```

---

### 5. 가상환경 실행

```bash
source .venv/bin/activate
```

가상환경이 정상 실행되면 터미널 앞에 `(.venv)`가 표시된다.

---

### 6. 패키지 설치

```bash
uv pip install -r requirements.txt
```

Django가 설치되었는지 확인하려면 다음 명령어를 사용한다.

```bash
python -m django --version
```

---

### 7. 기본 DB 생성

가상환경이 실행된 상태라면 아래 명령어를 사용한다.

```bash
python manage.py migrate
```

또는 `uv run`을 사용하려면 다음처럼 실행한다.

```bash
uv run python manage.py migrate
```

---

### 8. 서버 실행

```bash
python manage.py runserver 8010
```

---

### 9. 브라우저 접속

서버 실행 후 브라우저에서 아래 주소로 접속한다.

```text
http://127.0.0.1:8010/
```

8001 포트로 실행했다면 아래 주소로 접속한다.

```text
http://127.0.0.1:8001/
```

---

## 전체 명령어 한 번에 정리

```bash
cd ~/2026_6-17_diconai

git clone -b 2026_7_21_source --single-branch https://github.com/handgonpo/2026_7_21_diconai.git 2026_7_21_source

cd 2026_7_21_source

uv venv

source .venv/bin/activate

uv pip install -r requirements.txt

python manage.py migrate

python manage.py runserver 8010
```

## 접속 주소

로그인 화면:

http://localhost:8010/accounts/login/

대시보드:

http://localhost:8010/dashboard/
