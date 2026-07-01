# diconai-remake

산재 예방 통합 관제 플랫폼을 Django 기초부터 다시 구현하기 위한 수업용 skeleton 프로젝트입니다.

## Lesson 01 목표

- 기존 프로젝트의 HTML, CSS, JavaScript 화면만 유지
- Docker, FastAPI, K8s, Celery, Redis, PostgreSQL, AI 모델 제거
- Django 기본 구조에서 accounts/login, dashboard 화면 렌더링
- 이후 수업 단계에서 models.py, views.py, API, WebSocket, AI 기능을 다시 구현

## 실행 방법

1. 가상환경 생성

python3 -m venv .venv

2. 가상환경 실행

source .venv/bin/activate

3. 패키지 설치

pip install -r requirements.txt

4. 기본 DB 생성

python manage.py migrate

5. 서버 실행

python manage.py runserver 8010

## 접속 주소

로그인 화면:

http://localhost:8010/accounts/login/

대시보드:

http://localhost:8010/dashboard/
