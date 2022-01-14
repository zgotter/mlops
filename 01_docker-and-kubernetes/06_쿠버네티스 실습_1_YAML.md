# 6. 쿠버네티스 실습 1 - YAML

## 6.1 YAML 이란?

- 데이터 직렬화에 쓰이는 포맷/양식 중 하나
- cf) 데이터 직렬화
  - 서비스간에 데이터를 전송할 때 쓰이는 포맷으로 변환하는 작업
  - ex) 쿠버네티스 마스터에게 요청을 보낼 때 사용

- 다른 데이터 직렬화 포맷
  - XML, JSON

- YAML 파일 포맷
  - `.yaml`, `.yml`




## 6.2 YAML 특징

### 6.2.1 가독성

- YAML은 **사람이 읽기 쉽도록** 디자인

- 예시) YAML 포맷

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: example
  spec:
    containers:
      - name: busybox
        image: busybox:1.25
  ```

- 예시) JSON 포맷

  ```json
  {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
      "name": "example"
    },
    "spec": {
      "containers": [
        {
          "name": "busybox",
          "image": "busybox:1.25"
  			}
      ]
  	}
  }
  ```



### 6.2.2 Widely-use

- kubernetes manifests 명세
- docker compose 명세
- ansible playbook 명세
- github action workflow 명세



### 6.2.3 Strict-Validation

- 줄 바꿈
- 들여쓰기
  - `Tab` vs `Space`



## 6.3 문법

### 6.3.1 Key-Value

- Recursive한 key-value pair의 집합

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: example
  spec:
    containers:
      - name: busybox
        image: busybox:1.25
  ```



### 6.3.2 주석

- `#`을 줄의 맨 앞에 작성하면 주석 처리됨

  ```yaml
  # kubernetes pod exmaple . apiVersion: v1
  kind: Pod
  metadata:
  name: example #. spec:
  #. containers:
      - name: busybox
        image: busybox:1.25
  ```



### 6.3.3 자료형

#### 6.3.3.1 string

```yaml
# 일반적인 문자열은 그냥 작성해도 되고, 따옴표로 감싸도 된다.
example: this is 1st string
example: "this is 1st string"

# 반드시 따옴표로 감싸주어야 하는 경우
# (1) 숫자를 문자열 타입으로 지정하고 싶은 경우
example: 123 # integer 타입으로 인식
example: "123" # string 타입으로 인식

# (2) `y`, `yes`, `true` 등의 YAML 예약어와 겹치는 경우
example: "y"

# (3) `:`, `{`, `}`, `,`, `#`, `*`, `=`, `\n` 등의 특수 문자를 포함한 경우
example: "a : b"
example: "a#bc*"
```



#### 6.3.3.2 integer

```yaml
# integer type
example: 123

# hexadecimal type: 0x로 시작
example: 0x1fff
```



#### 6.3.3.3 float

```yaml
# float type
example: 99.9

# exponential type
example: 1.23e+03 # 1.23 x 10^3 = 1230
```



#### 6.3.3.4 boolean

```yaml
# True: true, yes, on
example: true
example: yes
example: on

# False: false, no, off
example: false
example: no
example: off
```



### 6.3.4 List

```yaml
# "-" 를 사용하여 list를 명시할 수 있음.
examples:
  - ex_one: 1
  - ex_two: 2

# "[]" 로 입력해도 됨.
examples: ["1", "2", "3"]

# list의 원소는 어떤 자료형이든 가능
spec:
  containers:
    - name: busybox
      image: busybox:1.25
    - name: ubuntu
      image: ubuntu
      commands:
        - sleep
        - 3600
    - name: python
      image: python:3.9
```



### 6.3.5 Multi-line strings

#### 6.3.5.1 `|`

- 중간에 위치한 **빈 줄**을 `\n`으로 처리하며, **문자열의 맨 마지막**에 `\n`을 붙인다.

  ```yaml
  example: |
  	Hello
  	First
  	Campus
  # "Hello\nFast\nCampus\n" 으로 처리
  ```



#### 6.3.5.2 `>`

- 중간에 위치한 **빈 줄**을 제외하고, **문자열의 맨 마지막**에 `\n` 을 붙인다.

  ```yaml
  example: >
  	Hello
  	First
  	Campus
  # "Hello Fast Campus\n" 으로 처리
  ```



#### 6.3.5.3 `|-`, `>-`

- `|`, `>` 와 동일하지만, **문자열의 맨 마지막**에 `\n` 이 추가되지 않음



### 6.3.6 Multi-document yaml

- `---` 이라는 구분선을 통해 하나의 yaml 파일에 여러 개의 yaml document를 작성할 수 있음

  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
  	name: one
  ---
  apiVersion: v1
  kind: Service
  metadata:
  	name: two
  ---
  apiVersion: v1
  kind: Deployment
  metadata:
  	name: three
  ```

  - 3개의 yaml document로 인식



### 6.3.7 복습

- Pod의 명세를 작성한 yaml 예시

  ```yaml
  # key-value pair
  apiVersion: v1
  kind: Pod
  metadata:
  	name: example
  	labels:
  		hello: bye
  spec:
  	containers:
  		# List
  		- name: busybox
  		  image: budybox:1.25
  		  ports:
  		  	- containerPort: 80
  		- name: another-container
  		  image: curlimages/curl
  ```

- 선언형 인터페이스를 위해서 Desired State를 명시하는 용도로 사용

