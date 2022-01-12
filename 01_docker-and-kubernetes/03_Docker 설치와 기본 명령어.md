# 3. Docker 설치와 기본 명령어

## 3.1 Docker 설치

### 3.1.1 Set up the repository

apt라는 패키지 매니저 업데이트

```bash
sudo apt-get update
```



docker의 prerequisite package들을 설치

```bash
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release
```



Docker의 GPG key 추가

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```



stable 버전의 repository를 바라보도록 설정

```bash
# 기본
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
# arm 기반의 cpu 사용 시
echo \
  "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```



### 3.1.2 Install Docker Engine

Docker 엔진의 최신 버전 설치

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```



### 3.1.3 정상 설치 확인

docker container를 실행시켜, 정상적으로 설치되었는 지 확인

```bash
sudo docker run hello-world
```



## 3.2 Docker 권한 설정

현재는 모든 docker 관련 작업이 root 유저에게만 권한이 있기 때문에, docker 관련 명령을 수행하려면 `sudo` 를 앞에 붙여주어야만 가능하다.

따라서, root 유저가 아닌 host의 기본 유저에게도 권한을 주기 위해 다음과 같은 명령을 **새로 띄운 터미널에서 수행해줘야 한다.**

```bash
sudo usermod -a -G docker $USER
sudo service docker restart
```



## 3.3 Docker의 기본적인 명령어

### 3.3.1 Docker pull

docker image repository로부터 docker image를 가져오는 명령어

예시)

```bash
docker pulll ubuntu:18.04
```

- [docker.io/library](http://docker.io/library/) 라는 이름의 repository 에서 ubuntu:18.04 라는 image 를 여러분의 노트북에 다운로드 받게된다.



참고 사항

- 추후 [docker.io](http://docker.io/) 나 public 한 docker hub 와 같은 repository 대신에, 특정 private 한 repository 에서 docker image 를 가져와야 하는 경우, docker login 을 통해서 특정 repository 를 바라보도록 한 뒤, docker pull 을 수행하는 형태로 사용한다.



### 3.3.2 Docker images

로컬에 존재하는 docker image 리스트를 출력하는 명령어

```bash
docker images
```



### 3.3.3 Docker ps

현재 실행중인 도커 컨테이너 리스트를 출력하는 명령어

```bash
docker ps # 실행중인 것들만
docker ps -a # 종료된 것 포함 전체
```



### 3.3.4 Docker run

도커 컨테이너를 실행시키는 명령어

예시)

```bash
docker run -it --name demo1 ubuntu:18.04 /bin/bash
```

- `-it`
  - `-i` 옵션 + `-t` 옵션
  - container를 실행시킴과 동시에 interactive한 terminal로 접속시켜주는 옵션
- `--name`
  - 컨테이너 id 대신 구분하기 쉽도록 지정해주는 이름
- `/bin/bash`
  - 컨테이너를 실행시킴과 동시에 실행할 명령어
  - `/bin/bash` 는 bash 터미널을 사용하는 것을 의미



### 3.3.5 Docker exec

Docker 컨테이너 내부에서 명령을 내리거나, 내부로 접속하는 명령어

예시)

```bash
# 컨테이너 실행
docker run -it -d --name demo2 ubuntu:18.04
```

- `-d` : 백그라운드에서 실행시켜서, 컨테이너에 접속 종료를 하더라도, 계속 실행 중이 되도록 하는 옵션

```bash
# 컨테이너 내부 접속
docker exec -it demo2 /bin/bash
```



### 3.3.6 Docker logs

도커 컨테이너의 log 를 확인하는 명령어

예시)

```bash
# 1초마다 현재시간을 출력하는 컨테이너 실행
docker run --name demo3 -d busybox sh -c "while true; do $(echo date); sleep 1; done"
```

- demo3 라는 이름의 busy box 이미지를 백그라운드에서 도커 컨테이너로 실행하여, 1초에 한 번씩 현재시간을 출력

```bash
docker logs demo3
docker logs demo3 -f
```

- `-f` : 계속 watch하며 출력하게 하는 옵션



### 3.3.7 Docker stop

실행 중인 도커 컨테이너를 중단시키는 명령어

```bash
docker stop demo3
docker stop demo2
docker stop demo1
```



### 3.3.8 Docker rm

도커 컨테이너를 삭제하는 명령어

```bash
docker rm demo3
docker rm demo2
docker rm demo1
```



### 3.3.9 Docker rmi

도커 이미지를 삭제하는 명령어

```bash
docker images
# busybox, ubuntu
docker rmi ubuntu
docker images
# busybox
```

