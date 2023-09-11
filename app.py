import base64
import io

import keras
import numpy as np
from flask import Flask, request, jsonify
from keras.utils import img_to_array, load_img

app = Flask(__name__)

model = keras.models.load_model('./model/model.h5')


@app.route('/predict-all', methods=['POST'])
def predict():
    content_type = request.content_type
    if content_type == "application/json":
        img_data = _to_bytes(base64.b64decode(request.get_json()["img"]))
    elif content_type == "application/x-www-form-urlencoded":
        img_data = _to_bytes(base64.b64decode(request.form.get("img")))
    elif content_type.startswith("multipart/form-data"):
        img_data = _to_bytes(request.files['img'].stream.read())
    else:
        img_data = _to_bytes(request.data)
    img = img_to_array(load_img(img_data, target_size=(28, 28), color_mode="grayscale")) / 255.
    img = np.expand_dims(img, axis=0)
    predict_x = model.predict(img)
    num = np.argmax(predict_x, axis=1)[0]
    probe = [float(x) for x in predict_x[0]]
    return jsonify({"probe": probe, "num": int(num)})


def _to_bytes(img):
    img_data = io.BytesIO()
    img_data.write(img)
    return img_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, debug=True)
