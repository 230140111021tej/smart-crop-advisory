# Smart Crop Advisory System 🌾

A beginner-friendly machine learning system that provides intelligent crop recommendations based on environmental and soil parameters. This system is designed for local experimentation with an emphasis on ML/data handling and future IoT/hardware extensibility.

## 🌟 Features

- **Machine Learning Model**: Random Forest classifier for crop prediction
- **Sample Dataset**: Pre-configured CSV dataset with various crop types
- **Training Pipeline**: Easy-to-use training script with evaluation metrics
- **REST API**: Flask-based API for real-time predictions
- **Beginner-Friendly**: Well-documented code with clear examples
- **IoT-Ready**: Designed with future hardware integration in mind

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/230140111021tej/smart-crop-advisory.git
cd smart-crop-advisory
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train.py
```

This will:
- Load the sample crop dataset
- Train a Random Forest model
- Evaluate model performance
- Save the trained model as `crop_model.pkl`

### 5. Start the API Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📊 Dataset

The `sample_crop_data.csv` contains the following features:

| Feature | Description | Unit |
|---------|-------------|------|
| temperature | Ambient temperature | °C |
| humidity | Relative humidity | % |
| ph | Soil pH level | pH scale (0-14) |
| rainfall | Annual rainfall | mm |
| soil_moisture | Soil moisture content | % |
| nitrogen | Nitrogen content in soil | kg/ha |
| phosphorus | Phosphorus content in soil | kg/ha |
| potassium | Potassium content in soil | kg/ha |
| crop | Target crop type (label) | - |

**Supported Crops**: Rice, Wheat, Maize, Cotton, Barley, Soybean, Sugarcane, Pulses, Millet, Groundnut, Potato, Tomato

## 🔌 API Usage

### Endpoints

#### 1. Home - API Information
```bash
GET http://localhost:5000/
```

#### 2. Health Check
```bash
GET http://localhost:5000/health
```

#### 3. Get Example Request
```bash
GET http://localhost:5000/example
```

#### 4. Predict Crop
```bash
POST http://localhost:5000/predict
Content-Type: application/json

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
```

### Example using cURL

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 25,
    "humidity": 60,
    "ph": 6.5,
    "rainfall": 80,
    "soil_moisture": 70,
    "nitrogen": 50,
    "phosphorus": 40,
    "potassium": 30
  }'
```

### Example using Python

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "temperature": 25,
    "humidity": 60,
    "ph": 6.5,
    "rainfall": 80,
    "soil_moisture": 70,
    "nitrogen": 50,
    "phosphorus": 40,
    "potassium": 30
}

response = requests.post(url, json=data)
print(response.json())
```

### Example Response

```json
{
  "recommended_crop": "Rice",
  "confidence": 0.95,
  "all_predictions": {
    "Rice": 0.95,
    "Wheat": 0.03,
    "Cotton": 0.01,
    "Soybean": 0.01,
    "Maize": 0.0
  },
  "input_parameters": {
    "temperature": 25,
    "humidity": 60,
    "ph": 6.5,
    "rainfall": 80,
    "soil_moisture": 70,
    "nitrogen": 50,
    "phosphorus": 40,
    "potassium": 30
  }
}
```

## 🔧 Project Structure

```
smart-crop-advisory/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
│
├── sample_crop_data.csv     # Sample training dataset
├── train.py                 # Model training script
├── app.py                   # Flask API application
│
└── crop_model.pkl           # Trained model (generated after training)
```

## 🔮 Future Enhancements

### IoT Integration
- Connect with soil sensors (pH, moisture, NPK)
- Temperature and humidity sensors
- Real-time data collection from field

### Hardware Compatibility
- Arduino/Raspberry Pi integration
- MQTT protocol support for sensor data
- Edge computing capabilities

### Advanced Features
- Historical data analysis
- Weather forecast integration
- Crop yield prediction
- Disease detection
- Multi-language support
- Mobile app integration

## 🧪 Extending the System

### Adding New Data
1. Add more samples to `sample_crop_data.csv`
2. Retrain the model: `python train.py`
3. Restart the API: `python app.py`

### Using Your Own Dataset
1. Replace `sample_crop_data.csv` with your dataset
2. Ensure it has the same column structure
3. Run `python train.py`

### Customizing the Model
Edit `train.py` to:
- Change model parameters
- Try different algorithms (SVM, XGBoost, Neural Networks)
- Add feature engineering
- Implement cross-validation

## 📝 Dependencies

- **Flask**: Web framework for API
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **joblib**: Model serialization

## 🐛 Troubleshooting

### Model Not Found Error
```
Error: Model file 'crop_model.pkl' not found!
```
**Solution**: Run `python train.py` to train and save the model first.

### Port Already in Use
```
Error: Address already in use
```
**Solution**: Change the port in `app.py` or kill the process using port 5000.

### Import Errors
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more crops to the dataset
- Improve model accuracy
- Add new features
- Fix bugs
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created for educational purposes and local experimentation with machine learning and IoT systems.

## 📧 Support

For questions or issues, please open an issue on GitHub.

---

**Happy Farming! 🌱**