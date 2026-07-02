# 브랜치 개발 로드맵

## 1. 현재 시작 상태

현재 프로젝트는 Django 초기 프로젝트에 HTML, CSS, JavaScript 화면 설계가 연결된 상태이다.

## 2. 0단계 브랜치

```text
lesson/00_project_baseline_20260721
```

목표:
```text
프로젝트 기준선 문서화
센서 데이터 정의
임계치 정의
샘플 이벤트 작성
최종 시연 시나리오 작성
패턴 적용 맵 작성
이후 브랜치 로드맵 확정
```

## 3. 이후 개발 브랜치

### Day 1. 화면 기준선 정리

1. lesson/01_01_template_static_structure
2. lesson/01_02_dashboard_layout_check
3. lesson/01_03_base_readme

### Day 2. 데이터 계약 설계

4. lesson/02_01_event_dictionary
5. lesson/02_02_sensor_event_schema
6. lesson/02_03_sample_event_json

### Day 3. 도메인 모델과 Raw 모델

7. lesson/03_01_domain_models
8. lesson/03_02_raw_models
9. lesson/03_03_migration_admin

### Day 4. Staging/Mart와 임계치

10. lesson/04_01_staging_models
11. lesson/04_02_mart_models
12. lesson/04_03_seed_thresholds

### Day 5. 시뮬레이터

13. lesson/05_01_basic_simulator
14. lesson/05_02_scenario_simulator
15. lesson/05_03_error_event_simulator

### Day 6. Collector 수집 API

16. lesson/06_01_collect_gas_api
17. lesson/06_02_collect_power_location_api
18. lesson/06_03_raw_save_api_test

### Day 7. 데이터 검증과 Dead Letter

19. lesson/07_01_raw_to_staging
20. lesson/07_02_validation_rules
21. lesson/07_03_dead_letter_events

### Day 8. 대시보드 데이터 연결

22. lesson/08_01_dashboard_view_context
23. lesson/08_02_sensor_cards_api
24. lesson/08_03_chart_recent_data

### Day 9. WebSocket 실시간 연결

25. lesson/09_01_channels_setup
26. lesson/09_02_sensor_ws_stream
27. lesson/09_03_dashboard_realtime_update

### Day 10. 지도와 지오펜스

28. lesson/10_01_leaflet_map_base
29. lesson/10_02_sensor_worker_marker
30. lesson/10_03_geofence_polygon_check

### Day 11. 위험도 판단 엔진

31. lesson/11_01_threshold_engine
32. lesson/11_02_geofence_risk_engine
33. lesson/11_03_risk_event_create

### Day 12. 알람과 피드백

34. lesson/12_01_alarm_record_create
35. lesson/12_02_alarm_dashboard_ui
36. lesson/12_03_feedback_action_log

### Day 13. AI 추론과 비동기 처리

37. lesson/13_01_ai_inference_service
38. lesson/13_02_ai_prediction_result
39. lesson/13_03_async_task_mock

### Day 14. 파이프라인, 품질, RAG

40. lesson/14_01_daily_summary_pipeline
41. lesson/14_02_data_quality_report
42. lesson/14_03_rag_manual_search

### Day 15. 운영 정리와 최종 시연

43. lesson/15_01_monitoring_metrics
44. lesson/15_02_docker_compose
45. lesson/15_03_final_demo_docs
