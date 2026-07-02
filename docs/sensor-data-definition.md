# 센서 데이터 정의

## 1. 유해가스 센서 데이터

유해가스 센서는 다음 값을 수집한다.

| 필드명 | 타입 | 단위 | 설명 |
|---|---|---|---|
| device_id | String | - | 기기 식별자 |
| device_name | String | - | 기기명 |
| software_version | String | - | 펌웨어 버전 |
| co | Number | ppm | 일산화탄소 농도 |
| h2s | Number | ppm | 황화수소 농도 |
| co2 | Number | ppm | 이산화탄소 농도 |
| o2 | Number | % | 산소 농도 |
| no2 | Number | ppm | 이산화질소 농도 |
| so2 | Number | ppm | 이산화황 농도 |
| o3 | Number | ppm | 오존 농도 |
| nh3 | Number | ppm | 암모니아 농도 |
| voc | Number | ppm | 휘발성유기화합물 농도 |
| measured_at | DateTime | - | 측정 시각 |

## 2. 스마트 파워 시스템 데이터

수업용 구현에서는 스마트 파워 시스템 데이터를 다음 구조로 단순화한다.

| 필드명 | 타입 | 단위 | 설명 |
|---|---|---|---|
| device_id | String | - | 기기 식별자 |
| channel_id | String | - | 채널 번호 |
| power_status | Number | - | 전원 상태 |
| current | Number | A | 전류 |
| voltage | Number | V | 전압 |
| power | Number | W | 전력 |
| measured_at | DateTime | - | 측정 시각 |

## 3. 작업자 위치 데이터

| 필드명 | 타입 | 단위 | 설명 |
|---|---|---|---|
| worker_id | String | - | 작업자 식별자 |
| worker_name | String | - | 작업자명 |
| x | Number | px 또는 meter | X 좌표 |
| y | Number | px 또는 meter | Y 좌표 |
| zone_id | String | - | 현재 구역 |
| measured_at | DateTime | - | 위치 측정 시각 |

## 4. 공통 이벤트 필드

모든 수집 이벤트는 다음 공통 필드를 가진다.

| 필드명 | 설명 |
|---|---|
| event_id | 이벤트 고유 ID |
| schema_version | 데이터 계약 버전 |
| source_system | 데이터 발생 시스템 |
| event_type | 이벤트 유형 |
| measured_at | 실제 측정 시각 |
| ingested_at | 서버 수집 시각 |
| quality_status | 데이터 품질 상태 |

## 5. 데이터 계약 방향

이 문서는 이후 다음 구현의 기준이 된다.

```text
Event Schema
Serializer
Raw Model
Validation Rule
Staging Model
Sample Event
```