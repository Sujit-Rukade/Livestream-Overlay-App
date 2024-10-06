from flask import Blueprint, jsonify, request

def create_stream_routes(mongo):
    stream_routes = Blueprint('stream_routes', __name__)

    @stream_routes.route('/stream', methods=['POST'])
    def set_rtsp_url():
        data = request.get_json()
        rtsp_url = data.get('rtsp_url')
        if rtsp_url:
            mongo.db.settings.update_one({}, {"$set": {"rtsp_url": rtsp_url}}, upsert=True)
            return jsonify({"message": "RTSP URL updated"}), 200
        else:
            return jsonify({"error": "RTSP URL missing"}), 400

    @stream_routes.route('/stream', methods=['GET'])
    def get_rtsp_url():
        settings = mongo.db.settings.find_one({}, {"rtsp_url": 1, "_id": 0})
        return jsonify(settings or {"rtsp_url": ""})

    return stream_routes
