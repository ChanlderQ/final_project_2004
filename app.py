import flask
from flask import Flask, jsonify,request, render_template, Response, redirect, url_for, request, session, abort
import json
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_end_predictions', methods=['post'])
def get_prediction_result():
    try:
        d1=float(request.json["Vertical_input"])
        d2=float(request.json["Diagonal_input"])
        d3=float(request.json["Cross_input"])
        d4=float(request.json["Height_input"])
        d5=float(request.json["Width_input"])
        input_data=np.array([d1,d2,d3,d4,d5]).reshape(1, -1)
        print(input_data)
        file = open("fish_model.pickle",'rb')
        model=pickle.load(file)
        pre_weight=model.predict(input_data)
        print("weight",pre_weight)
        return app.response_class(response=json.dumps(pre_weight[0]), status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        print(err)
        return app.response_class(response=json.dumps(pre_weight[0]), status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=False)