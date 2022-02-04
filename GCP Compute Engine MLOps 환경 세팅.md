# GCP Compute Engine MLOps 환경 세팅

## 1. GCP Compute Engine 인스턴스 생성

- Ubuntu 20.04



## 2. 인스턴스 ssh 연결

### 2.1 공개키 생성

```bash
ssh-keygen -t rsa -b 4096 -f gcp_rsa_4096 -C shkim4738@gmail.com
```

- `-t` : key 생성 타입 (`rsa`)
- `-b` : type의 bytes 설정 (default: 2048)
- `-f` : 생성할 key의 이름
- `-C` : 주석 입력



### 2.2 공개키 내용 복사

- `.pub` 확장자로 끝나는 공개키의 내용을 복사

```bash
cat gcp_rsa_4096.pub > pub_key.txt
```



### 2.3 메타데이터 > SSH 키 등록

- 위에서 복사한 내용을 Compute Engine > 설정 > 메타데이터 > SSH 키에 등록



### 2.4 ssh 연결

```bash
ssh -i gcp_rsa_4096 shkim4738@인스턴외부IP주소
```



## 3. Docker 설치

```bash
sudo apt-get update

# 필요 패키지 설치
sudo apt-get install \
ca-certificates \
curl \
gnupg \
lsb-release

# GPG key 등록
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# stable repository set up
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

# docker engine 설치
sudo apt-get install docker-ce docker-ce-cli containerd.io

# docker 권한 설정
sudo usermod -a -G docker $USER
sudo service docker restart

# ssh 접속 해제 후 재연결
exit

# docker 정상 설치 확인
docker ps
```



## 4. Kubernetes 환경 설치

### 4.1 minikube 설치

```bash
curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube version
```



### 4.2 kubectl 설치

```bash
curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version
```