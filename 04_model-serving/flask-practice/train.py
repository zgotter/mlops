import os
import pickle

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

RANDOM_SEED = 1234

# Step 1) data load
data = load_iris()

# Step 2) data split
X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED)

# Step 3) train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=RANDOM_SEED
)
model.fit(X_train, y_train)

# Step 4) evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Step 5) save model to ./build/model.pkl
os.makedirs("./build", exist_ok=True)
pickle.dump(model, open("./build/model.pkl", "wb"))