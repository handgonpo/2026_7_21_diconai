# 데이터 엔지니어링 패턴 적용 맵

## 1. 목적

이 문서는 디코나이 관제 플랫폼 개발 과정에서 데이터 엔지니어링 디자인 패턴을 어디에 적용할지 정리한다.

## 2. 패턴 적용 요약

| 패턴 영역 | 적용 위치 | 프로젝트 적용 예시 |
|---|---|---|
| 데이터 수집 | Sensor Simulator, Collector API | 전체 로더, 증분 로더, 외부 트리거 |
| 오류 관리 | Staging Validation | Dead Letter, 중복 제거, 지연 데이터 탐지 |
| 멱등성 | Raw 저장, Alarm 생성 | event_id 기반 중복 방지, 알람 병합 |
| 데이터 가치 | Risk Engine | 센서값 + 임계치 조인, 작업자 위치 + 지오펜스 조인 |
| 데이터 흐름 | Collector, Risk Engine, Dashboard | fan-in, fan-out, 이벤트 분기 |
| 데이터 보안 | 관리자/작업자/알람 데이터 | 권한 분리, 작업자 식별정보 최소화 |
| 데이터 스토리지 | Raw/Staging/Mart | 원본 보존, 검증 데이터, 대시보드용 Mart |
| 데이터 품질 | Validation, Report | null 검증, 범위 검증, schema_version 관리 |
| 관찰가능성 | DataOps Report | 수집 중단, 지연, 오류 건수 추적 |

## 3. 이후 구현 기준

이 문서는 이후 다음 단계의 구현 기준이 된다.

```text
Staging Validation
Dead Letter Table
Risk Engine
Alarm Deduplication
Data Quality Report
Event Trace
```