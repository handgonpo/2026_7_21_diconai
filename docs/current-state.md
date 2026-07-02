# 현재 프로젝트 상태

## 1. 현재 브랜치

lesson/00_project_baseline_20260721

## 2. 현재 구현 상태

현재 프로젝트는 Django 기반으로 초기화되어 있으며, 화면 설계를 위한 HTML, CSS, JavaScript가 Template/Static 구조로 연결되어 있다.

현재 구현된 범위는 다음과 같다.

- Django 프로젝트 초기화
- views.py 작성
- urls.py 작성
- HTML Template 연결
- CSS Static 연결
- JavaScript Static 연결
- 대시보드 화면 껍데기 구성

## 3. 현재 없는 기능

현재는 다음 기능이 아직 구현되어 있지 않다.

- 센서 데이터 모델
- Raw/Staging/Mart 테이블
- 가짜 데이터 생성기
- 수집 API
- WebSocket
- 위험도 판단 로직
- 알람 저장
- AI 추론
- RAG 검색
- 데이터 품질 리포트
- 운영 모니터링
- Docker 실행 환경

## 4. 현재 상태의 의미

현재 프로젝트는 디코나이 관제 플랫폼의 화면 설계를 위한 초기 화면 구조이다.
이후 개발에서는 이 화면 구조를 유지하면서, 데이터 계약, 수집 API, 저장 계층, 위험도 판단, 알람, AI, RAG, DataOps 기능을 단계적으로 추가한다.