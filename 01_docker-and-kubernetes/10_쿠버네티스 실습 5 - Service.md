# 10. 쿠버네티스 실습 5 - Service

## 10.1 Service 란?

- Service는 쿠버네티스에 배포한 애플리케이션(Pod)을 외부에서 접근할 수 있도록 추상화한 리소스이다.
- [쿠버네티스 공식 문서 - Service](https://kubernetes.io/ko/docs/concepts/services-networking/service/)
- Pod는 IP를 할당받고 생성되지만, 언제든지 죽었다가 다시 살아날 수 있으며, 그 과정에서 IP는 항상 재할당 받기 떄문에 고정된 IP로 원하는 Pod에 접근할 수 없다.
- 따라서 클러스터 외부 혹은 내부에서 Pod에 접근할 때는, Pod의 IP가 아닌 Service를 통해서 접근하는 방식을 사용한다.
- Service는 고정된 IP를 가지며, Service는 하나 또는 여러 개의 Pod과 매칭된다.
- 따라서 클라이언트가 Service의 주소(endpoint)로 접근하면, 실제로는 Service에 매칭된 Pod에 접속할 수 있게 된다.



## 10.2 Service 생성 및 확인

### 10.2.1 Deployment 생성

```yaml
# deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

```bash
kubectl apply -f deployment.yaml
```



### 10.2.2 Pod IP 확인

```bash
# Pod의 IP 확인
kubectl get pod -o wide
```



### 10.2.3 외부에서 Pod IP로 접속 시도

```bash
# 접속 시도
curl -X GET <pod-ip> -vvv
ping <pod-ip>
# -> 통신 불가
```

- 할당된 `<pod-ip>` 는 클러스터 내부에서만 접근할 수 있는 IP 이기 때문에 외부에서는 Pod에 접속할 수 없다.



### 10.2.4 minikube 내부에서 통신 시도

minikube 내부로 접속하면 통신이 되는 지 확인

```bash
# minikube 내부로 접속
minikube ssh

# 접속 시도
curl -X GET <pod-ip> -vvv
ping <pod-ip>
# -> 통신 가능
```



### 10.2.5 Service 생성

위에서 생성한 Deployment를 매칭시킨 Service 생성

```yaml
# service.yaml

apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  type: NodePort # Service의 Type을 명시하는 부분 (10.3 에서 설명)
  ports:
  - port: 80
    protocol: TCP
  selector: # 아래 label을 가진 Pod을 매핑하는 부분
    app: nginx
```

```bash
vi service.yaml

# 위 내용 붙여넣기

# service 적용
kubectl apply -f service.yaml
```



### 10.2.6 Service 확인

```bash
kubectl get service
```

- PORT `80:<port>` 숫자를 확인할 수 있다.



### 10.2.7 Service를 통해 Pod 접속

```bash
curl -X GET $(minikube ip):<port>
```

- 이렇게 서비스를 통해서 클러스터 외부에서도 정상적으로 Pod에 접속할 수 있는 것을 확인할 수 있다.



## 10.3 Service의 Type

### 10.3.1 `NodePort`

- `NodePort` 라는 type을 사용했기 때문에 minikube라는 kubernetes cluster 내부에 배포된 서비스에 클러스터 외부에서 접근할 수 있다.
  - 접근하는 IP는 Pod가 떠 있는 노드(머신)의 IP를 사용하고, Port는 Service가 할당받은 Port를 사용한다.
- `NodePort`  type은 Pod가 어떤 노드에 스케쥴링될 지 모르는 상황에서, Pod가 할당된 후 해당 노드의 IP를 알아야 한다는 단점이 존재한다.



### 10.3.2 `LoadBalancer`

- `LoadBalancer` 라는 type을 사용해도 마찬가지로 클러스터 외부에서 접근할 수 있다.
- 하지만 LoadBalancing 역할을 하는 모듈이 추가적으로 필요하다.



### 10.3.3 `ClusterIP`

- `ClusterIP` 라는 type은 고정된 IP, PORT를 제공하지만, 이 IP와 PORT는 클러스터 내부에서만 접근할 수 있는 대역의 주소가 할당된다.



### 10.3.4 실무에서의 Service Type

- 실무에서는 주로 kubernetes cluster에 MetalLB와 같은 LoadBalancing 역할을 하는 모듈을 설치한 후, `LoadBalancer` type으로 서비스를 expose하는 방식을 사용한다.

