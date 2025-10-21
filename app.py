"""
Smart Crop Advisory System - Flask API

This is a minimal Flask API that provides crop recommendations based on
environmental and soil parameters using a pre-trained ML model.
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Global variable to store the model
model = None
MODEL_PATH = 'crop_model.pkl'


def load_model():
    """Load the trained model from disk."""
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
        return True
    else:
        print(f"Warning: Model file '{MODEL_PATH}' not found!")
        print("Please run 'python train.py' first to train and save the model.")
        return False


@app.route('/')
def home():
    """Home endpoint with API information."""
    return jsonify({
        'name': 'Smart Crop Advisory System API',
        'version': '1.0.0',
        'description': 'ML-powered crop recommendation system',
        'endpoints': {
            '/': 'API information (this page)',
            '/health': 'Health check endpoint',
            '/predict': 'POST endpoint for crop prediction'
        },
        'model_loaded': model is not None
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict the most suitable crop based on input parameters.
    
    Expected JSON input:
    {
        "temperature": 25,
        "humidity": 60,
        "ph": 6.5,
        "rainfall": 80,
        "soil_moisture": 70,
        "nitrogen": 50,
        "phosphorus": 40,
        "potassium": 30
    }
    """
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first using train.py'
        }), 503
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = [
            'temperature', 'humidity', 'ph', 'rainfall',
            'soil_moisture', 'nitrogen', 'phosphorus', 'potassium'
        ]
        
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Prepare input features in the correct order
        features = np.array([[
            data['temperature'],
            data['humidity'],
            data['ph'],
            data['rainfall'],
            data['soil_moisture'],
            data['nitrogen'],
            data['phosphorus'],
            data['potassium']
        ]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get prediction probabilities if available
        try:
            probabilities = model.predict_proba(features)[0]
            classes = model.classes_
            
            # Create a dictionary of crop probabilities
            crop_probabilities = {
                crop: float(prob) for crop, prob in zip(classes, probabilities)
            }
            
            # Sort by probability
            sorted_crops = sorted(
                crop_probabilities.items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            response = {
                'recommended_crop': prediction,
                'confidence': float(max(probabilities)),
                'all_predictions': dict(sorted_crops[:5]),  # Top 5
                'input_parameters': data
            }
        except AttributeError:
            # If model doesn't support predict_proba
            response = {
                'recommended_crop': prediction,
                'input_parameters': data
            }
        
        return jsonify(response)
    
    except Exception as e:
        # Log the error for debugging but don't expose details to users
        print(f"Prediction error: {str(e)}")
        return jsonify({
            'error': 'Prediction failed. Please check your input parameters.'
        }), 500


@app.route('/example')
def example():
    """Provide an example request for testing."""
    return jsonify({
        'description': 'Example input for /predict endpoint',
        'method': 'POST',
        'content_type': 'application/json',
        'example_request': {
            'temperature': 25,
            'humidity': 60,
            'ph': 6.5,
            'rainfall': 80,
            'soil_moisture': 70,
            'nitrogen': 50,
            'phosphorus': 40,
            'potassium': 30
        },
        'curl_example': (
            'curl -X POST http://localhost:5000/predict '
            '-H "Content-Type: application/json" '
            '-d \'{"temperature":25,"humidity":60,"ph":6.5,"rainfall":80,'
            '"soil_moisture":70,"nitrogen":50,"phosphorus":40,"potassium":30}\''
        )
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Smart Crop Advisory System - Flask API")
    print("=" * 60)
    
    # Try to load the model
    if load_model():
        print("\nAPI is ready to serve predictions!")
    else:
        print("\nAPI will start, but predictions won't work until model is trained.")
    
    print("\nStarting Flask server...")
    print("API will be available at: http://localhost:5000")
    print("=" * 60)
    
    # Use debug mode only in development. Set to False in production.
    # You can control this with environment variables
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
