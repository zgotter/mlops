# 2. Prometheus & Grafana

## 2.1 Prometheus

> Prometheus is a free software application used for event monitoring and alerting - Wikipedia

- [https://github.com/prometheus](https://github.com/prometheus)



### 2.1.1 Prometheus란?

- 2012년 CoundCloud에서 만든 모니터링 & 알람 프로그램
- 2016년 CNCF에 Joined, 2018년 Graduated 하여 완전 독립형 오픈소스 프로젝트로 발전
- 쿠버네티스에 종속적이지 않고, binary 혹은 docker container 형태로도 사용하고 배포 가능
- 쿠버네티스 생태계의 오픈소스 중에서는 사실상의 표준
  - pull 방식의 구조가 쿠버네티스와 궁합이 맞고, 다양한 플러그인 제공



### 2.1.2 특징

- 수집하는 Metric 데이터를 다차원(Multi dimensional)의 시계열 데이터 형태로 저장

- 데이터 분석을 위한 자체 언어 PromQL 지원

- 시계열 데이터 저장에 적합한 TimeSeries DB 지원

- **데이터 수집하는 방식**이 Push 방식이 아닌 **Pull 방식을 사용**
- Push 방식
    - 모니터링 대상의 Agent가 서버로 Metric을 보내는 방식
  - Pull 방식
  - 서버가 Agent로부터 직접 정보를 가져가는 방식
  - Pull 방식에 단점이 존재하기 때문에 Push 방식을 위한 Push Gateway도 지원

- 다양한 시각화 툴(ex. Grafana)과의 연동 지원

- 다양한 방식(ex. Slack, e-mail)의 Alarming 지원



### 2.1.3 구조

<div><img src="https://prometheus.io/assets/architecture.png" /></div>



#### 2.1.3.1 Prometheus Server

- 시계열 데이터를 수집하고 TSDB에 저장
- 설치 시 metrics 수집 주기를 정할 수 있다. (default: 15초)



#### 2.1.3.2 Service Discovery

- Monitoring 대상 리스트 조회
- 사용자는 Monitoring 대상 리스트를 쿠버네티스에 등록
- Prometheus Server는 쿠버네티스 API Server에게 모니터링 대상을 물어보는 형태



#### 2.1.3.3 Exporter

- Prometheus가 metrics을 수집해갈 수 있도록 정해진 HTTP Endpoint를 제공하여 정해진 형태로 metrics를 Export
- Prometheus Server가 이 Exporter의 Endpoint로 HTTP GET Request를 보내 metrics를 pull하여 저장한다.
- 하지만, 이런 pull 방식은 수집 주기와 네트워크 단절 등의 이유로 모든 metrics 데이터 수집을 보장할 수 없기 때문에 push 방식을 위한 Pushgateway 제공



#### 2.1.3.4 Pushgateway

- 보통 Prometheus Server의 pull 주기(period)보다 짧은 lifecycle을 지닌 작업의 metrics 수집을 보장하기 위해 사용됨



#### 2.1.3.5 AlertManager

- PromQL을 사용해 특정 조건문을 만들고, 해당 조건문이 만족되면 정해진 방식으로 정해진 메세지를 보낼 수 있음
- ex) service A가 5분간 응답이 없으면, 관리자에게 DM과 e-mail을 보낸다.



#### 2.1.3.6 Grafana

- Prometheus와 항상 함께 연동되는 시각화 툴
- Prometheus 자체 UI도 있고, API 제공을 하기에 직접 시각화 대시보드를 구성할 수도 있음



#### 2.1.3.7 PromQL

- Prometheus가 저장한 데이터 중 원하는 정보만 가져오기 위한 Query Language 제공
- Time Series 데이터이며, Multi-Demensional 데이터이기 때문에 처음 보면 다소 복잡할 수 있음
- Prometheus 및 Grafana를 잘 사용하기 위해서는 어느 정도 익혀두어야 함
- [Querying basic | Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)



### 2.1.4 단점

- Scalability, High Availability 보장의 어려움
  - Prometheus Server가 Single Node로 운영되어야 하기 때문에 발생하는 문제
  - [Thanos](https://thanos.io/) 라는 오픈 소스를 활용해 multi prometheus server를 운영할 수 있다.



## 2.2 Grafana

> The open and composable observability and data visualization platform. - grafana

- [https://github.com/grafana/grafana](https://github.com/grafana/grafana)



### 2.2.1 Grafana란?

- 2014년 릴리즈된 프로젝트로 처음에는 InfluxDB, Prometheus와 같은 TimeSeriesDB 전용 시각화 툴로 개발되었으나, 이후 MySQL, PostgreSQL 과 같은 RDB도 지원
- 현재는 Grafana Labs 회사에서 관리하고 있으며, 오픈 소스 프로젝트인 Grafana 외에도 상용 서비스인 Grafana Cloud, Grafana Enterprise 제품 존재
  - 상용 서비스는 추가 기능 제공과 설치 및 운영 등의 기술 지원까지 포함
- [playground 페이지](https://play.grafana.org/d/000000012/grafana-play-home?orgId=1)도 제공하여 쉽고 간편하게 Grafana Dashboard를 사용해볼 수 있음
- 쿠버네티스에 종속적이지 않고, Docker로 쉽게 설치할 수 있음
- 여러 Datasource와의 연동성이 뛰어나고, 특히 Prometheus와의 연동이 뛰어남



### 2.2.2 다양한 외부 Plugins

- [https://grafana.com/grafana/plugins/](https://grafana.com/grafana/plugins/)



### 2.2.3 다양한 Grafana Dashboard

- [https://grafana.com/grafana/dashboards/](https://grafana.com/grafana/dashboards/)



### 2.2.4 Grafana Dashboard 모범 사례

- 수많은 metric 중 모니터링해야 할 대상을 정하고 어떤 방식으로 시각화할 것인지에 대한 정답은 없다.
  - task 마다 요구사항이 달라지기 때문

- Google에서 제시한 전통 SW 모니터링을 위한 4가지 황금 지표

  - Latency
    - 사용자가 요청 후 응답을 받기까지 걸린 시간

  - Traffic
    - 시스템이 처리해야 하는 총 부하

  - Errors
    - 사용자의 요청 중 실패한 비율

  - Saturation
    - 시스템의 포화 상태

- ML 기반의 서비스를 모니터링할 때도 위 4가지 지표를 염두에 두고 대시보드를 구성하는 것을 권장
- 다만 처음 시작할 때는 위의 다양한 오픈소스 대시보드 중 하나를 import하는 것부터 시작

