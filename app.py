from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("isolation_forest_model.pkl")

@app.route('/')
def home():
    return "Anomaly Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    pred = model.predict(df)
    result = [1 if i == -1 else 0 for i in pred]
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
