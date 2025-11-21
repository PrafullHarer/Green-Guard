# Green Guard - Plant Disease Detection

A Flask-based web application that uses a Keras deep learning model to detect plant diseases from uploaded images.

## Features

- **AI-Powered Disease Detection**: Upload plant images and get instant disease diagnosis
- **Comprehensive Disease Information**: Get detailed information about causes and treatments
- **Modern UI**: Beautiful, responsive interface with real-time updates
- **Multiple Crop Support**: Detects diseases in various crops including tomatoes, potatoes, apples, grapes, and more
- **Advisory Hub**: Includes crop advice, irrigation planning, market info, tool catalogues, government schemes, and team/about pages to build user trust
- **Weather-aware Workflows**: Uses WeatherAPI data (via `WEATHER_API_KEY`) to contextualize recommendations and future irrigation/DAS logic

## Architecture Overview

Green Guard follows a classic Flask MVC layout:

1. **Presentation layer**: HTML templates under `templates/` plus themed CSS/JS in `static/` provide responsive UI modules (home, crop advice, markets, irrigation, schemes, profile, etc.).
2. **Application layer**: `app.py` wires routes, handles uploads, validates files, fetches weather data, and orchestrates predictions with TensorFlow.
3. **AI inference layer**: A TensorFlow/Keras model (`model/plant_disease_recog_model_pwp.keras`) classifies diseases and is paired with `plant_disease.json` for human-readable metadata (cause/cure).
4. **Data layer**: An in-memory database stub in `db_utils.py` captures user and disease records. It can later be swapped with MongoDB/Firestore following the collection/index definitions in `config.py`.

The upload flow sanitizes filenames, enforces formats (`png`, `jpg`, `jpeg`), limits file size (16 MB), performs prediction, then schedules hourly cleanup of temporary files. Static previews served from `/uploadimages/<filename>` keep result pages lightweight.

## Configuration & Environment

Create a `.env` file (or set environment variables in your shell) before running the app:

```
WEATHER_API_KEY=your_weather_api_key
TWILIO_ACCOUNT_SID=optional_twilio_sid
TWILIO_AUTH_TOKEN=optional_twilio_token
TWILIO_PHONE_NUMBER=optional_twilio_number
```

Key configuration toggles live in `config.py`:

- `UPLOAD_FOLDER`, `ALLOWED_EXTENSIONS`, `MAX_CONTENT_LENGTH`
- Named Mongo-style collections and indexes (`USERS_COLLECTION`, `CROPS_COLLECTION`, etc.) for future persistence layers
- API keys for WeatherAPI (required) and Twilio (optional SMS alerts; integration currently commented out)

When deploying, make sure to override `SECRET_KEY` in `app.py` and point `UPLOAD_FOLDER` to a persistent storage volume.

## Setup Instructions

### Prerequisites


- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   - Open your web browser
   - Go to `http://localhost:5000`
   - Navigate to the disease detection page

## Usage

1. **Upload Image**: Click "Choose File" and select a plant image (PNG, JPEG, or WebP format)
2. **Analyze**: Click "Analyze Image" to process the image
3. **View Results**: Get the disease diagnosis, confidence level, cause, and treatment recommendations

## Supported Crops and Diseases

The model can detect diseases in:
- **Tomatoes**: Bacterial spot, Early blight, Late blight, Leaf mold, Septoria leaf spot, Spider mites, Target spot, Yellow leaf curl virus, Mosaic virus
- **Potatoes**: Early blight, Late blight
- **Apples**: Apple scab, Black rot, Cedar apple rust
- **Grapes**: Black rot, Esca (Black measles), Leaf blight
- **Corn**: Gray leaf spot, Common rust, Northern leaf blight
- **Cherries**: Powdery mildew
- **Peaches**: Bacterial spot
- **Bell Peppers**: Bacterial spot
- **Strawberries**: Leaf scorch

## Technical Details

- **Backend**: Flask web framework
- **AI Model**: Keras deep learning model (`plant_disease_recog_model_pwp.keras`)
- **Image Processing**: PIL (Python Imaging Library)
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap

## File Structure

```
Green-Guard/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── model/
│   └── plant_disease_recog_model_pwp.keras  # Keras model
├── templates/
│   ├── disease.html               # Disease detection page
│   └── ...                       # Other HTML templates
├── static/
│   ├── css/
│   │   └── disease.css           # Disease page styling
│   ├── js/
│   └── uploads/                  # Uploaded images storage
└── README.md                     # This file
```

## Troubleshooting

### Common Issues

1. **Model Loading Error**: Ensure the Keras model file is in the `model/` directory
2. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in `app.py` or stop other applications using port 5000

### Performance Tips

- Use images with clear, well-lit plant parts
- Ensure the plant part (leaf, fruit, etc.) is clearly visible
- For best results, use images with good resolution (minimum 224x224 pixels)

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the UI/UX
- Adding support for more crops and diseases

## License

This project is open source and available under the MIT License. 
