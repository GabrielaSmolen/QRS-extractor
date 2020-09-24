from flask import Flask, jsonify, request
from utils.base_objects import QRS
import logging
import json
import numpy as np
from ecg_analysis import qrs_analysis

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/predict", methods=["POST"])
def predict():
    logging.info('Request received')
    if request.method == 'POST':
        posted_data = request.get_json()
        data = json.loads(posted_data['samples'])
        data = np.array(data)
        qrs = QRS(data)
        qrs.process()
        result = qrs.get_label()
        logging.info('Processing done. Predicted label {}'.format(result))
        return jsonify(str("QRS label is " + str(result)))


@app.route("/detect", methods=["POST"])
def detect():
    logging.info('Request received')
    if request.method == 'POST':
        posted_data = request.get_json()
        samples = json.loads(posted_data['samples'])
        samples = np.array(samples)
        fs = 360
        morphology, detected_indices = qrs_analysis(samples, fs)
        result = {}
        for m, d in zip(morphology, detected_indices):
            result.append("m" == d)
        logging.info('Processing done. Predicted morphology labels: {}'.format(result))
        return jsonify(str("QRS morphology labels are " + str(result)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
