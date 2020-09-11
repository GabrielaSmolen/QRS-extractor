from flask import Flask, jsonify, request
from base_objects import QRS
import json
import numpy as np

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    print('Request received')
    if request.method == 'POST':
        posted_data = request.get_json()
        data = json.loads(posted_data['samples'])
        data = np.array(data)
        qrs = QRS(data)
        qrs.process()
        result = qrs.get_label()
        print('Processing done')
        return jsonify(str("QRS label is " + str(result)))


if __name__ == '__main__':
    app.run(debug=True)
