# AI 네이티브 데이터 플랫폼 엔지니어 과정
- 중기청 유해가스 관제 플랫폼을 기반으로 한 실시간 데이터 수집·정규화·AI 이상탐지·운영 배포 실습

## 전체 개발순서

```
→ 데이터 계약 정의
→ Raw 저장
→ Staging 검증/정규화
→ Mart 집계/위험판정
→ AI 이상탐지
→ 실시간 알림
→ Docker 운영
→ Prometheus/Grafana 관측
→ Kubernetes 배포
```

## 수업 브랜치 운영 방법
이 저장소는 AI 네이티브 데이터 플랫폼 엔지니어 과정 수업을 단계별로 따라갈 수 있도록 브랜치 단위로 관리합니다.
각 브랜치는 하나의 수업 단원을 의미하며, 수업이 진행될 때마다 새로운 브랜치를 생성하여 해당 단계의 코드와 문서를 업로드합니다.

## 수업 브랜치 운영 방법

이 저장소는 `AI 네이티브 데이터 플랫폼 엔지니어 과정` 수업을 단계별로 따라갈 수 있도록 브랜치 단위로 관리합니다.

각 브랜치는 하나의 수업 단원을 의미하며, 수업이 진행될 때마다 새로운 브랜치를 생성하여 해당 단계의 코드와 문서를 업로드합니다.

---

## 1. 수업 브랜치 이름 규칙

브랜치 이름은 다음 규칙을 사용합니다.

```bash
lesson/주차번호_수업주제_날짜
```

예시:

```bash
lesson/01_data-contract_20260618
lesson/02_raw-ingestion_20260619
lesson/03_staging-normalization_20260620
lesson/04_mart-risk-evaluation_20260621
lesson/05_ai-anomaly-detection_20260622
lesson/06_realtime-alert_20260623
lesson/07_docker-monitoring_20260624
lesson/08_kubernetes-deploy_20260625
```

> 브랜치명에는 공백을 넣지 않습니다.
> 한글보다는 영문 소문자, 숫자, 하이픈(`-`), 언더바(`_`) 사용을 권장합니다.

---

## 2. 강사용: 새 수업 브랜치 만드는 방법

### 2-1. 최신 main 브랜치로 이동

```bash
git checkout main
git pull origin main
```

또는 Git 최신 버전에서는 다음 명령어를 사용할 수 있습니다.

```bash
git switch main
git pull origin main
```

---

### 2-2. 새 수업 브랜치 생성

예시: 1주차 데이터 계약 정의 수업 브랜치 생성

```bash
git checkout -b lesson/01_data-contract_20260618
```

또는:

```bash
git switch -c lesson/01_data-contract_20260618
```

---

### 2-3. 수업 코드와 문서 작성 후 변경 사항 확인

```bash
git status
```

---

### 2-4. 변경 파일 추가

전체 파일을 추가할 경우:

```bash
git add .
```

특정 파일만 추가할 경우:

```bash
git add README.md
git add docs/lessons/01_data_contract.md
git add backend_drf/
git add generator_fastapi/
```

---

### 2-5. 커밋 생성

```bash
git commit -m "lesson 01: define sensor data contract"
```

커밋 메시지 예시:

```bash
git commit -m "lesson 02: implement raw sensor data ingestion"
git commit -m "lesson 03: add staging validation and normalization"
git commit -m "lesson 04: add mart risk evaluation logic"
git commit -m "lesson 05: connect AI anomaly detection pipeline"
```

---

### 2-6. GitHub에 브랜치 업로드

```bash
git push origin lesson/01_data-contract_20260618
```

이후 GitHub 저장소에서 해당 브랜치를 선택하면 수업 단계별 코드를 확인할 수 있습니다.

---

## 3. 학생용: 수업 브랜치별 코드 내려받는 방법

학생은 수업 주차에 맞는 브랜치를 선택하여 코드를 내려받으면 됩니다.

---

## 방법 1. 저장소를 처음 받는 경우

특정 브랜치만 바로 내려받으려면 다음 명령어를 사용합니다.

```bash
git clone -b 브랜치명 --single-branch 저장소주소
```

예시:

```bash
git clone -b lesson/01_data-contract_20260618 --single-branch https://github.com/handgonpo/diconai-projects.git
```

폴더명을 직접 지정하고 싶다면 마지막에 폴더명을 붙입니다.

```bash
git clone -b lesson/01_data-contract_20260618 --single-branch https://github.com/handgonpo/diconai-projects.git diconai-lesson01
```

---

## 방법 2. 저장소 전체를 받은 뒤 브랜치 이동하기

전체 저장소를 먼저 내려받습니다.

```bash
git clone https://github.com/handgonpo/diconai-projects.git
```

프로젝트 폴더로 이동합니다.

```bash
cd diconai-projects
```

원격 브랜치 목록을 확인합니다.

```bash
git branch -r
```

원하는 수업 브랜치로 이동합니다.

```bash
git switch lesson/01_data-contract_20260618
```

만약 브랜치가 바로 보이지 않으면 다음 명령어로 원격 브랜치 정보를 갱신합니다.

```bash
git fetch --all
```

그 후 다시 브랜치로 이동합니다.

```bash
git switch lesson/01_data-contract_20260618
```

---

## 방법 3. 이미 저장소를 받은 학생이 다음 수업 브랜치로 이동하는 경우

기존 프로젝트 폴더로 이동합니다.

```bash
cd diconai-projects
```

최신 브랜치 정보를 가져옵니다.

```bash
git fetch --all
```

원하는 수업 브랜치로 이동합니다.

```bash
git switch lesson/02_raw-ingestion_20260619
```

해당 브랜치의 최신 코드를 가져옵니다.

```bash
git pull origin lesson/02_raw-ingestion_20260619
```

---

## 4. 현재 내가 어떤 브랜치에 있는지 확인하기

```bash
git branch
```

현재 사용 중인 브랜치 앞에는 `*` 표시가 붙습니다.

예시:

```bash
* lesson/01_data-contract_20260618
  main
```

---

## 5. 전체 수업 브랜치 목록 확인하기

로컬 브랜치 확인:

```bash
git branch
```

원격 브랜치까지 모두 확인:

```bash
git branch -a
```

원격 브랜치만 확인:

```bash
git branch -r
```

---

## 6. 수업 단계별 개발 흐름

본 과정은 중기청 유해가스 관제 플랫폼을 기반으로 다음 순서로 개발합니다.

```text
데이터 계약 정의
→ Raw 저장
→ Staging 검증/정규화
→ Mart 집계/위험판정
→ AI 이상탐지
→ 실시간 알림
→ Docker 운영
→ Prometheus/Grafana 관측
→ Kubernetes 배포
```

각 단계는 별도의 `lesson` 브랜치로 관리합니다.

예시:

| 단계  | 브랜치 예시                                     | 수업 내용                 |
| --- | ------------------------------------------ | --------------------- |
| 1단계 | `lesson/01_data-contract_20260618`         | 센서 데이터 계약 정의          |
| 2단계 | `lesson/02_raw-ingestion_20260619`         | 원본 Raw 데이터 저장         |
| 3단계 | `lesson/03_staging-normalization_20260620` | 데이터 검증 및 정규화          |
| 4단계 | `lesson/04_mart-risk-evaluation_20260621`  | Mart 집계 및 위험 판정       |
| 5단계 | `lesson/05_ai-anomaly-detection_20260622`  | AI 이상탐지 결과 연동         |
| 6단계 | `lesson/06_realtime-alert_20260623`        | WebSocket 실시간 알림      |
| 7단계 | `lesson/07_docker-monitoring_20260624`     | Docker 기반 통합 실행       |
| 8단계 | `lesson/08_kubernetes-deploy_20260625`     | Kubernetes 배포 및 운영 검증 |

---

## 7. 학생 실습 권장 흐름

학생은 각 수업마다 다음 순서로 실습합니다.

```bash
git fetch --all
git switch 수업브랜치명
git pull origin 수업브랜치명
```

예시:

```bash
git fetch --all
git switch lesson/03_staging-normalization_20260620
git pull origin lesson/03_staging-normalization_20260620
```

이후 README 또는 `docs/lessons/` 폴더의 수업 문서를 참고하여 실습을 진행합니다.

---

## 8. 브랜치 사용 시 주의사항

수업 브랜치에서 개인 실습 코드를 수정한 경우, 다음 브랜치로 이동할 때 충돌이 발생할 수 있습니다.

현재 변경 사항을 확인하려면 다음 명령어를 사용합니다.

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

## 9. 추천 브랜치 운영 원칙

```text
main = 최종 완성본
lesson/* = 수업 단계별 코드
docs/lessons/* = 각 수업 설명 문서
```

브랜치는 매번 무작정 생성하지 않고, 하나의 수업 단원이 완성될 때마다 생성합니다.

```text
좋은 예:
lesson/01_data-contract_20260618
lesson/02_raw-ingestion_20260619

나쁜 예:
test1
new
update
final
final-real
final-real-last
```

브랜치 이름만 보아도 어떤 수업 단계인지 알 수 있도록 관리합니다.
