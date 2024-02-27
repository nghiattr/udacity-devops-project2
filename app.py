from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
import json

app = Flask(__name__)

# Load your trained machine learning model
model = RandomForestRegressor()  # Example model, replace with your own

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract feature values from the nested dictionaries
    features = [float(val["0"]) for val in data.values()]

    # Here you can add your prediction logic based on the received data
    # For demonstration purposes, let's assume a simple prediction based on the sum of the features
    prediction = sum(features)

    return jsonify({"prediction": prediction}), 200


if __name__ == '__main__':
    app.run(debug=True)
