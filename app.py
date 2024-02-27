from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
import json
import pandas as pd

app = Flask(__name__)

# Load your trained machine learning model
model = joblib.load('path_to_your_saved_model.pkl')  # Example model, replace with your own

# Example route for machine learning prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()

    # Preprocess the data as needed
    # Example: Convert JSON data to DataFrame for prediction
    # Assuming the JSON data contains features for prediction
    features = pd.DataFrame.from_dict(data, orient='index').T
    
    # Perform prediction
    prediction = model.predict(features)
    
    # Format prediction result as JSON
    result = {'prediction': prediction.tolist()}  # Convert prediction to list for JSON serialization
    
    # Return prediction result as JSON payload
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
