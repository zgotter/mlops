# 1. MLOps에서 쿠버네티스가 필요한 이유

## 1.1 MLOps를 위해 필요한 3가지 작업

- Reproducibility
  - 실행 환경의 일관성 & 독립성
- Job Scheduling
  - 머신러닝 학습 스케줄 관리
  - 병렬 작업 관리
  - 유휴 자원 관리
- Auto-healing & Auto-scaling
  - 학습 서버 및 배포 서버 장애 대응
  - 트래픽 대응



## 1.2 Docker & Kubernetes

도커와 쿠버네티스를 사용하면 위와 같은 작업들을 쉽게 할 수 있다.

- docker
  - Containerization
- kubernetes
  - Container Orchestration



## 1.3 Containerization

- Containerization
  - 컨테이너화 하는 기술
  - 나의 머신러닝 코드를 OS나 파이썬 환경, pip 패키지 버전 등과 같은 것들에 독립적이도록 하는 정보를 모두 담은 실행 환경 자체를 하나의 패키지로 만드는 기술
- Container
  - 격리된 공간에서 프로세스를 실행시킬 수 있는 기술



## 1.4 Container Orchestration

- 여러 개의 컨테이너들을 지휘하는 기술
- ex) 수많은 도커 컨테이너들을 역할에 맞는 서버에 배치시키는 것을 조율
- 쿠버네티스가 container orchestration의 표준 기술로 자리잡았다.