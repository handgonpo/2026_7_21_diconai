# AI 네이티브 데이터 플랫폼 엔지니어 과정

중기청 유해가스 관제 플랫폼을 기반으로 한  
**실시간 데이터 수집·저장·검증·위험도 판단·AI 이상탐지·운영 배포 실습 프로젝트**입니다.

이 저장소는 수업을 단계별로 따라갈 수 있도록 브랜치 단위로 관리합니다.

---

## 1. 프로젝트 목표

본 프로젝트의 목표는 단순한 웹사이트를 만드는 것이 아니라,  
AI가 사용할 데이터를 안정적으로 수집하고 운영하는 **AI 네이티브 데이터 플랫폼 흐름**을 구현하는 것입니다.

수업에서는 실제 장비를 직접 연결하지 않고, 수업용 가짜 데이터를 생성하여 다음 흐름을 구현합니다.

```text
Sensor Simulator
→ Collector API
→ Raw 저장
→ Staging 검증/정규화
→ Mart 생성/위험도 판단
→ Alarm Service
→ Dashboard
→ AI 이상탐지
→ RAG 대응 매뉴얼
→ Data Quality Report
→ Docker / Monitoring / 배포 확장
```

---

## 2. 수업에서 다루는 데이터

| 데이터 | 예시 | 사용 목적 |
|---|---|---|
| 유해가스 데이터 | CO, H2S, CO2, O2 등 | 가스 위험도 판단 |
| 전력 데이터 | 전류, 전압, 전력, 전원 상태 | 장비 이상 감지 |
| 작업자 위치 데이터 | worker_id, x, y, zone_id | 위험구역 진입 판단 |

---

## 3. 전체 개발 흐름

본 과정은 다음 순서로 개발합니다.

```text
0단계: 프로젝트 기준선 문서화
1단계: Django 화면 구조 정리
2단계: 데이터 구조 정의
3단계: DB 모델과 Raw 데이터 저장
4단계: 데이터 검증과 Mart 데이터 생성
5단계: Sensor Simulator와 Collector API
6단계: 위험도 판단과 알람 생성
7단계: 대시보드 데이터 연결
8단계: WebSocket 실시간 반영
9단계: 지도와 지오펜스
10단계: AI 이상탐지, RAG, 데이터 품질 리포트 확장
11단계: Docker, Monitoring, 배포 구조 확장
12단계: 최종 시연과 운영 문서화
```

자세한 개발 순서는 다음 문서에서 관리합니다.

```text
docs/branch-roadmap.md
```

---

## 4. 브랜치 운영 방식

이 저장소는 수업 단계를 브랜치 단위로 관리합니다.

```text
main
→ 전체 프로젝트 소개와 기준 안내

2026_7_21_source
→ 수업 시작 전 초기 소스 기준 브랜치

lesson/*
→ 수업 단계별 코드와 문서 브랜치
```

각 브랜치는 하나의 수업 단원 또는 실습 단위를 의미합니다.

---

## 5. 브랜치 이름 규칙

브랜치 이름은 다음 규칙을 사용합니다.

```text
lesson/단계번호_세부번호_수업주제
```

예시:

```text
lesson/00_project_baseline_20260721
lesson/01_01_template_static_structure
lesson/01_02_dashboard_layout_check
lesson/02_01_event_dictionary
lesson/02_02_sensor_event_schema
lesson/03_01_domain_models
lesson/03_02_raw_models
lesson/04_01_staging_models
lesson/04_03_seed_thresholds
lesson/05_01_basic_simulator
lesson/06_01_collect_gas_api
lesson/07_01_raw_to_staging
lesson/08_01_dashboard_view_context
lesson/09_01_channels_setup
lesson/10_01_leaflet_map_base
lesson/11_01_threshold_engine
lesson/12_01_alarm_record_create
lesson/13_01_ai_inference_service
lesson/14_02_data_quality_report
lesson/15_03_final_demo_docs
```

브랜치명에는 공백을 넣지 않습니다.  
영문 소문자, 숫자, 하이픈(`-`), 언더바(`_`) 사용을 권장합니다.

---

## 6. 새 수업 브랜치 생성 방법

최신 `main` 브랜치로 이동합니다.

```bash
git switch main
git pull origin main
```

새 수업 브랜치를 생성합니다.

```bash
git switch -c lesson/00_project_baseline_20260721
```

변경 사항을 확인합니다.

```bash
git status
```

변경 파일을 추가합니다.

```bash
git add .
```

커밋합니다.

```bash
git commit -m "docs: define project baseline"
```

GitHub에 브랜치를 업로드합니다.

```bash
git push -u origin lesson/00_project_baseline_20260721
```

---

## 7. 학생용 브랜치 이동 방법

저장소를 처음 받는 경우:

```bash
git clone https://github.com/handgonpo/2026_7_21_diconai.git
cd 2026_7_21_diconai
```

원격 브랜치 정보를 가져옵니다.

```bash
git fetch --all
```

원하는 수업 브랜치로 이동합니다.

```bash
git switch lesson/00_project_baseline_20260721
```

해당 브랜치의 최신 내용을 가져옵니다.

```bash
git pull origin lesson/00_project_baseline_20260721
```

---

## 8. 현재 브랜치 확인 방법

```bash
git branch
```

현재 사용 중인 브랜치 앞에는 `*` 표시가 붙습니다.

예시:

```text
* lesson/00_project_baseline_20260721
  main
```

원격 브랜치까지 모두 확인하려면 다음 명령어를 사용합니다.

```bash
git branch -a
```

---

## 9. 주요 문서 구조

```text
README.md
→ 현재 브랜치의 핵심 안내

docs/
→ 프로젝트 기준 문서와 수업 설계 문서

sample_events/
→ 수업용 샘플 이벤트 JSON

seed/
→ 초기 기준 데이터
```

주요 문서 예시는 다음과 같습니다.

```text
docs/current-state.md
docs/project-overview.md
docs/project-scope.md
docs/sensor-data-definition.md
docs/threshold-definition.md
docs/system-context.md
docs/final-demo-scenario.md
docs/pattern-application-map.md
docs/branch-roadmap.md
```

---

## 10. 실행 방법

가상환경을 생성합니다.

```bash
python -m venv .venv
```

가상환경을 실행합니다.

Windows PowerShell:

```bash
.venv\Scripts\activate
```

macOS / Linux / WSL:

```bash
source .venv/bin/activate
```

패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

Django 서버를 실행합니다.

```bash
python manage.py runserver
```

브라우저에서 다음 주소로 접속합니다.

```text
http://127.0.0.1:8000/
```

---

## 11. 브랜치 사용 시 주의사항

수업 브랜치에서 개인 실습 코드를 수정한 경우, 다음 브랜치로 이동할 때 충돌이 발생할 수 있습니다.

현재 변경 사항을 확인합니다.

```bash
git status
```

수정한 내용을 임시 저장하려면 다음 명령어를 사용합니다.

```bash
git stash
```

다른 브랜치로 이동한 뒤 임시 저장한 내용을 다시 적용하려면 다음 명령어를 사용합니다.

```bash
git stash pop
```

수업 중에는 강사의 안내 없이 `main` 브랜치에 직접 코드를 수정하지 않는 것을 권장합니다.

---

## 12. 최종 시연 목표

최종 시연은 기능 목록이 아니라 **데이터가 흐르는 장면**으로 보여줍니다.

```text
1. Sensor Simulator가 센서 데이터를 생성한다.
2. Collector API가 데이터를 수집한다.
3. DB에 데이터가 저장된다.
4. 위험도 판단 기준에 따라 normal / warning / danger가 결정된다.
5. 위험 상태가 발생하면 알람이 생성된다.
6. 대시보드에 센서 상태와 알람이 표시된다.
7. 작업자가 위험구역에 들어가면 지오펜스 알람이 발생한다.
8. 이후 AI 이상탐지, RAG 대응 매뉴얼, 데이터 품질 리포트로 확장한다.
```

---

## 13. 추천 브랜치 운영 원칙

```text
main = 전체 프로젝트 소개와 기준 안내
2026_7_21_source = 수업 시작 전 초기 소스
lesson/* = 수업 단계별 코드와 문서
docs/* = 프로젝트 기준 문서
sample_events/* = 샘플 이벤트 데이터
seed/* = 초기 기준 데이터
```

좋은 브랜치명 예시:

```text
lesson/00_project_baseline_20260721
lesson/01_01_template_static_structure
lesson/02_01_event_dictionary
lesson/03_01_domain_models
```

피해야 할 브랜치명 예시:

```text
test1
new
update
final
final-real
final-real-last
```

브랜치 이름만 보아도 어떤 수업 단계인지 알 수 있도록 관리합니다.
