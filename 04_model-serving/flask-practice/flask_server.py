import pickle

import numpy as np
from flask import Flask, jsonify, request

# 학습한 모델 파일을 불러온다.
model = pickle.load(open("./build/model.pkl", "rb"))

# Flask Server 구현
app = Flask(__name__)

# POST /predict API 구현
@app.route("/predict", methods=["POST"])
def make_predict():
    # API Request Body를 python dictionary object로 변환
    request_body = request.get_json(force=True)

    # request body를 model의 형식에 맞게 변환
    X_test = [
        request_body["sepal_length"],
        request_body["sepal_width"],
        request_body["petal_length"],
        request_body["petal_width"],
    ]
    X_test = np.array(X_test)
    X_test = X_test.reshape(1, -1)

    # model의 predict 함수를 호출하여 prediction 값을 구함
    y_test = model.predict(X_test)

    # prediction 값을 json화
    response_body = jsonify(result=y_test.tolist())

    # predict 결과를 담아 API Response Body를 return
    return response_body

if __name__ == "__main__":
    app.run(port=5000, debug=True)
