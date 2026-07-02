# 시스템 컨텍스트

## 1. 현재 시작 구조

현재 프로젝트는 Django 기반 화면 프로젝트이다.

```text
Browser
→ Django URL
→ Django View
→ Template
→ Static CSS/JS
→ Dashboard 화면 표시


## 2. 목표 시스템 구조
```text
Sensor Simulator
→ Collector API
→ Raw Table
→ Staging Validation
→ Mart Table
→ Risk Engine
→ Alarm Service
→ Dashboard
→ Feedback
→ AI Inference
→ RAG Manual Search
→ Data Quality Report


## 3. 현재 구조와 목표 구조의 차이

| 구분 | 현재 | 목표 |
|---|---|---|
| 데이터 | 없음 | 센서/전력/위치 이벤트 |
| 저장 | 없음 | Raw/Staging/Mart |
| 판단 | 없음 | Threshold + Geofence |
| 알람 | 없음 | AlarmRecord |
| AI | 없음 | AIPredictionResult |
| RAG | 없음 | Manual Search |
| 품질 | 없음 | Data Quality Report |
| 화면 | HTML/CSS/JS | 실시간 관제 대시보드 |

## 4. Mermaid 구조도

```mermaid
flowchart LR
    A[Sensor Simulator] --> B[Collector API]
    B --> C[Raw Tables]
    C --> D[Staging Validation]
    D --> E[Mart Tables]
    E --> F[Risk Engine]
    F --> G[Alarm Service]
    G --> H[Dashboard]
    G --> I[Feedback Logs]
    F --> J[AI Inference]
    G --> K[RAG Manual Search]
    C --> L[Data Quality Report]