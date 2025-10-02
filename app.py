import os
import random
import uuid
import json
import time
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
# from twilio.rest import Client  # Removed Twilio import
import requests
import logging
from config import Config
from db_utils import db
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH
app.config['ALLOWED_EXTENSIONS'] = Config.ALLOWED_EXTENSIONS

# Ensure upload directory exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
 

# WeatherAPI Key
WEATHER_API_KEY = Config.WEATHER_API_KEY

try:
    model = tf.keras.models.load_model(os.path.join("model", "plant_disease_recog_model_pwp.keras"))
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

try:
    with open("plant_disease.json", 'r', encoding='utf-8') as file:
        content = file.read().strip()
        plant_disease = json.loads(content) if content else {}
        if not content:
            logger.warning("plant_disease.json is empty; continuing with empty mapping")
except Exception as e:
    logger.error(f"Failed to read plant_disease.json: {e}")
    plant_disease = {}

# Helper functions

def _check_access(template_name: str):
    return render_template(template_name)

def extract_features(image_path):
    try:
        image = tf.keras.utils.load_img(image_path, target_size=(160, 160))
        img_array = tf.keras.utils.img_to_array(image)
        return np.array([img_array])
    except Exception as e:
        logger.error(f"Error extracting features from image: {str(e)}")
        raise ValueError("Invalid or corrupted image file")

def model_predict(image_path):
    if model is None:
        return {"name": "Model not available"}
    features = extract_features(image_path)
    prediction = model.predict(features)
    idx = int(np.argmax(prediction[0]))
    
    # Debug logging
    logger.info(f"Model predicted class: {idx}")
    logger.info(f"Total disease classes available: {len(plant_disease) if isinstance(plant_disease, list) else 'Not a list'}")
    
    # plant_disease is now a list, access by index
    if isinstance(plant_disease, list) and 0 <= idx < len(plant_disease):
        entry = plant_disease[idx]
        logger.info(f"Found disease entry for class {idx}: {entry.get('name', 'Unknown')}")
        return entry
    elif isinstance(plant_disease, dict):
        # Fallback for dictionary format
        entry = plant_disease.get(str(idx))
        logger.info(f"Looking for class '{idx}' in dict, found entry: {entry}")
        if isinstance(entry, dict):
            return entry
        if isinstance(entry, str):
            return {"name": entry}
    
    # Enhanced fallback with more information
    confidence = float(np.max(prediction[0]))
    logger.warning(f"Class {idx} not found in disease database. Confidence: {confidence:.2f}")
    return {
        "name": f"Class {idx}",
        "cause": f"AI model classified this as class {idx} with {confidence:.1%} confidence, but detailed information is not available in our database.",
        "cure": "Please consult with a plant specialist for proper diagnosis and treatment recommendations."
    }

# Routes
@app.route('/DAS')
def DAS():
    return render_template('DAS.html')

@app.route('/DAS.html')
def DAS_html():
    return render_template('DAS.html')

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/home')
def home_redirect():
    return redirect(url_for('index'))



#login and register
@app.route('/login.html')
def login():
    return render_template('login.html')
 
@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route("/forget_password")
def forget_password():
    return render_template("forget_password.html")

@app.route("/reset_password")
def reset_password():
    return render_template("reset_password.html")

@app.route("/logout.html")
def logout():
    # For now, just redirect to login page
    return render_template("login.html")



#disease prediction
@app.route('/disease')
def disease():
    return render_template('disease.html', result=False)

@app.route('/disease.html')
def disease_html():
    return render_template('disease.html', result=False)

# Alias route in case of pluralized path usage
@app.route('/diseases.html')
def diseases_alias():
    return render_template('disease.html', result=False)


#map market
@app.route("/market.html")
def market():
    return _check_access("market.html")



#irrigation market and tools
@app.route("/irrigation.html")
def irrigation():
    return _check_access("irrigation.html")



#tools market
@app.route("/tools.html")
def tools():
    return _check_access("tools.html")




#seeds market
@app.route("/seeds.html")
def seeds():
    return _check_access("seeds.html")



#seeds and equipment market
@app.route("/market1.html")
def market1():
    return _check_access("market1.html")

@app.route("/equipment.html")
def equipment():
    return render_template("tools.html")



#crop advice
@app.route("/crop_advice.html")
def crop_advice():
    return _check_access("crop_advice.html")

@app.route("/sugarcane.html")
def sugarcane():
    return _check_access("crops/sugarcane.html")

@app.route("/rice.html")
def rice():
    return _check_access("crops/rice.html")

@app.route("/wheat.html")
def wheat():
    return _check_access("crops/wheat.html")

@app.route("/onion.html")
def onion():
    return _check_access("crops/onion.html")

@app.route("/tomato.html")
def tomato():
    return _check_access("crops/tomato.html")

@app.route("/potato.html")
def potato():
    return _check_access("crops/potato.html")

@app.route("/cabbage.html")
def cabbage():
    return _check_access("crops/cabbage.html")

@app.route("/ladii.html")
def ladii():
    return _check_access("crops/ladii.html")

@app.route("/chilli.html")
def chilli():
    return _check_access("crops/chilli.html")

@app.route("/garlic.html")
def garlic():
    return _check_access("crops/garlic.html")



#govt schemes
@app.route("/schemes.html")
def schemes():
    return _check_access("schemes.html")


#profile
@app.route("/profile.html")
def profile():
    return _check_access("profile.html")

@app.route("/edit_profile.html")
def edit_profile():
    return _check_access("edit_profile.html")


#about us
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/team.html")
def team():
    return render_template("team.html")

@app.route("/uploadimages/<path:filename>")
def uploaded_images(filename):
    try:
        return send_from_directory(Config.UPLOAD_FOLDER, filename)
    except Exception as e:
        logger.error(f"Error serving image: {str(e)}")
        return "Image not found", 404

@app.route("/upload/", methods=["POST", "GET"])
def uploadimage():
    """
    Handle plant image upload and disease prediction
    Supports both GET and POST requests
    """
    if request.method == "POST":
        try:
            # Check if file is present in request
            if 'img' not in request.files:
                flash("No image file found. Please select an image to upload.", "danger")
                return redirect(url_for('disease'))
            
            image = request.files["img"]
            
            # Check if filename is empty
            if image.filename == '':
                flash("No image selected. Please choose an image file.", "danger")
                return redirect(url_for('disease'))
            
            # Validate file extension
            if not image.filename.lower().endswith(tuple(Config.ALLOWED_EXTENSIONS)):
                flash(f"Invalid file format. Only {', '.join(Config.ALLOWED_EXTENSIONS).upper()} files are allowed.", "danger")
                return redirect(url_for('disease'))
            
            # Check file size (16MB limit)
            try:
                image.seek(0, 2)  # Seek to end of file
                file_size = image.tell()
                image.seek(0)  # Reset file pointer
                
                if file_size > Config.MAX_CONTENT_LENGTH:
                    flash(f"File too large. Maximum size allowed is {Config.MAX_CONTENT_LENGTH // (1024*1024)}MB.", "danger")
                    return redirect(url_for('disease'))
            except (OSError, IOError) as e:
                logger.error(f"Error checking file size: {str(e)}")
                flash("Error reading file. Please try with a different image.", "danger")
                return redirect(url_for('disease'))
            
            # Check if model is available
            if model is None:
                flash("AI model is not available. Please try again later.", "danger")
                return redirect(url_for('disease'))
            
            # Generate unique filename
            original_filename = secure_filename(image.filename)
            file_extension = os.path.splitext(original_filename)[1]
            unique_filename = f"temp_{uuid.uuid4().hex}{file_extension}"
            filepath = os.path.join(Config.UPLOAD_FOLDER, unique_filename)
            
            # Ensure upload directory exists
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
            
            # Save uploaded file
            image.save(filepath)
            logger.info(f"Image saved successfully: {unique_filename}")
            
            # Basic image validation - try to open the saved file
            try:
                test_image = tf.keras.utils.load_img(filepath, target_size=(160, 160))
                test_image.close()
            except Exception as validation_error:
                logger.error(f"Image validation failed: {str(validation_error)}")
                if os.path.exists(filepath):
                    os.remove(filepath)
                flash("Invalid image file. Please upload a valid image.", "danger")
                return redirect(url_for('disease'))
            
            # Perform disease prediction
            try:
                prediction = model_predict(filepath)
                logger.info(f"Prediction completed: {prediction.get('name', 'Unknown')}")
                
                # Clean up old temporary files (optional - remove files older than 1 hour)
                cleanup_old_files()
                
                # Render results
                return render_template("disease.html", 
                                    result=True, 
                                    imagepath=f"/uploadimages/{unique_filename}", 
                                    prediction=prediction,
                                    filename=original_filename)
                                    
            except Exception as prediction_error:
                logger.error(f"Prediction error: {str(prediction_error)}")
                # Clean up uploaded file if prediction fails
                if os.path.exists(filepath):
                    os.remove(filepath)
                flash("Error analyzing the image. Please try with a different image.", "danger")
                return redirect(url_for('disease'))
                
        except Exception as e:
            logger.error(f"Upload error: {str(e)}")
            flash("An error occurred while processing your image. Please try again.", "danger")
            return redirect(url_for('disease'))
    
    # Handle GET requests - redirect to disease page
    return redirect(url_for('disease'))


def cleanup_old_files():
    """
    Clean up temporary files older than 1 hour
    """
    try:
        current_time = time.time()
        one_hour_ago = current_time - 3600  # 1 hour in seconds
        
        for filename in os.listdir(Config.UPLOAD_FOLDER):
            if filename.startswith('temp_'):
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                if os.path.isfile(filepath):
                    file_time = os.path.getmtime(filepath)
                    if file_time < one_hour_ago:
                        os.remove(filepath)
                        logger.info(f"Cleaned up old file: {filename}")
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)