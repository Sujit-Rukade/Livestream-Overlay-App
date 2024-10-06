from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId

def create_overlay_routes(mongo):
    overlay_routes = Blueprint('overlay_routes', __name__)

    @overlay_routes.route('/overlays', methods=['POST'])
    def create_overlay():
        data = request.get_json()

        overlay_data = {
            "data": {
                "position": {
                    "x": data.get("data", {}).get("position", {}).get("x", 0),
                    "y": data.get("data", {}).get("position", {}).get("y", 0)
                },
                "size": data.get("data", {}).get("size", "16px"),
                "color": data.get("data", {}).get("color", "white"),
                "text": data.get("data", {}).get("text", "Overlay Text"),
                "opacity": data.get("data", {}).get("opacity", 1.0),
                "border": data.get("data", {}).get("border", "none")
            }
        }

        overlay_id = mongo.db.overlays.insert_one(overlay_data).inserted_id
        return jsonify({"message": "Overlay created", "overlay_id": str(overlay_id)})

    @overlay_routes.route('/overlays', methods=['GET'])
    def get_overlays():
        overlays = list(mongo.db.overlays.find())
        return jsonify([
            {
                "_id": str(overlay["_id"]),
                "data": overlay.get("data", {})
            } for overlay in overlays
        ])

    @overlay_routes.route('/overlays/<id>', methods=['PUT'])
    def update_overlay(id):
        data = request.get_json()
        overlay_update_data = {
            "data": {
                "position": {
                    "x": data.get("data", {}).get("position", {}).get("x"),
                    "y": data.get("data", {}).get("position", {}).get("y")
                },
                "size": data.get("data", {}).get("size"),
                "color": data.get("data", {}).get("color"),
                "text": data.get("data", {}).get("text"),
                "opacity": data.get("data", {}).get("opacity"),
                "border": data.get("data", {}).get("border")
            }
        }

        mongo.db.overlays.update_one({"_id": ObjectId(id)}, {"$set": overlay_update_data})
        return jsonify({"message": "Overlay updated"})

    @overlay_routes.route('/overlays/<id>', methods=['DELETE'])
    def delete_overlay(id):
        mongo.db.overlays.delete_one({"_id": ObjectId(id)})
        return jsonify({"message": "Overlay deleted"})

    return overlay_routes
