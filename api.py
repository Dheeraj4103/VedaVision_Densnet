from flask import Flask, request, jsonify
from flask_cors import CORS
from trail import getPlant

app = Flask(__name__)

CORS(app)

@app.route('/', methods=["GET"])
def home():
    response = {"message": "This is VedaVision Chatbot"}
    return jsonify(response)

@app.route('/predict', methods=['POST'])
def predict():
    query = request.get_json()
    preprocessed_image = query.get("imgArray")
    try:
        result = getPlant(preprocessed_image)
    except:
        result = []
    return jsonify({"idxs": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
