from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def get_prediction():
    # Unique instance identifier
    instance_id = socket.gethostbyname(socket.gethostname())
    return jsonify({'message': 'Prediction made', 'instance_id': instance_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)