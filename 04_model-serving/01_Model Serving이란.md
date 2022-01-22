# 1. Model Serving 이란

## 1.1 Serving 이란?

- ML Model을 서비스화하는 것



## 1.2 서비스 제공 방식

- HTTP API Request
- 챗봇과의 대화
- Netflix 영상 좋아요 버튼
- Youtube 구독 버튼
- 네이버 길찾기 버튼



## 1.3 서빙 단계에서 막히는 이유

- 모델 개발과 소프트웨어 개발의 방법의 괴리
- 모델 개발 과정과 소프트웨어 개발 과정의 파편화
- 모델 평가 방식 및 모니터링 구축의 어려움



## 1.4 서빙의 간편화를 도와주는 도구

- Seldon Core
- TFServing
- KFServing
- Torch Serve
- BentoML



## 1.5 Flask & Seldon Core

- flask, fastapi, django와 같은 파이썬 기반의 REST API 프레임워크를 사용해서 머신러닝 모델 코드를 감싼 API 서버를 개발
- 해당 API 서버를 dockerize한 다음 배포
- 그 앞단에 load balancer를 붙임

