# 디코나이 관제 플랫폼 프로젝트 개요

## 1. 프로젝트명

디코나이 AI 네이티브 산업안전 관제 플랫폼

## 2. 프로젝트 목적

본 프로젝트는 유해가스 센서, 스마트 파워 시스템, 작업자 위치 데이터를 수집하여 산업 현장의 위험 상태를 실시간으로 판단하고, 대시보드와 알람을 통해 관리자에게 제공하는 AI 기반 산업안전 관제 플랫폼을 개발하는 것을 목표로 한다.

단순히 데이터를 화면에 보여주는 대시보드가 아니라, 데이터가 생성되는 순간부터 수집, 저장, 검증, 위험도 판단, 알람, AI 이상탐지, RAG 대응 매뉴얼, 운영 피드백, 데이터 품질 관리까지 연결되는 AI 네이티브 데이터 플랫폼으로 구현한다.

## 3. 최종 개발 목표

최종적으로 다음 흐름이 동작하는 시스템을 만든다.

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