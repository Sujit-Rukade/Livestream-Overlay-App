from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from overlay_routes import create_overlay_routes
from stream_routes import create_stream_routes  # Import Stream Routes

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/overlayDB"
mongo = PyMongo(app)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Initialize and Register Blueprints for Overlay and Stream Routes
overlay_routes = create_overlay_routes(mongo)
stream_routes = create_stream_routes(mongo)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Livestream Overlay API"}), 200  # Return a status code

# Register the blueprints (routes)
app.register_blueprint(overlay_routes, url_prefix='/api')  # You can prefix the API
app.register_blueprint(stream_routes, url_prefix='/api')  # You can prefix the API

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Set host and port explicitly
