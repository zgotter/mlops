from flask import Flask
import json

app = Flask(__name__)

@app.route("/predict", methods=["POST", "PUT"])
def inference():
    return json.dumps({"hello": "world"}), 200 # http status code를 200으로 반환하는 것을 의미

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
