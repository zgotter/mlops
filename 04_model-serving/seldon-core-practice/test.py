import numpy as np

from seldon_core.seldon_client import SeldonClient

sc = SeldonClient(
    gateway="ambassador",
    transport="rest",
    gateway_endpoint="127.0.0.1:80",
    namespace="seldon"
)

client_prediction = sc.predict(
    data=np.array([[1, 2, 3, 4]]),
    deployment_name="iris-model",
    names=["text"],
    payload_type="ndarray"
)

print(client_prediction)