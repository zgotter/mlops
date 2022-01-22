from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # debug 모드로 실행
    # 모든 IP에서 접근 허용
    # 5000 포트 사용