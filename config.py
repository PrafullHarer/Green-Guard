import os

class Config:
    
    # Collection Names
    USERS_COLLECTION = "users"
    CROPS_COLLECTION = "crops"
    WEATHER_COLLECTION = "weather_data"
    DISEASE_COLLECTION = "disease_records"
    
    # Indexes Configuration
    INDEXES = {
        USERS_COLLECTION: [
            {"key": [("email", 1)], "unique": True},
            {"key": [("phone", 1)]},
            {"key": [("created_at", 1)]}
        ],
        CROPS_COLLECTION: [
            {"key": [("name", 1)], "unique": True},
            {"key": [("season", 1)]}
        ],
        DISEASE_COLLECTION: [
            {"key": [("user_id", 1)]},
            {"key": [("date", 1)]}
        ]
    }
    
    # API Keys
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '4067ebad8ace4cacac9134438242510')

    
    # File Upload Configuration
    UPLOAD_FOLDER = "uploadimages"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size 
