import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request

# the name of the app(flask()):
app = Flask(__name__)
MODEL = pickle.load(open('churn_model.pkl', 'rb'))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/predict_churn", methods=["GET"])
def get_prediction():
    is_male = request.args.get("is_male")
    num_inters = request.args.get("num_inters")
    late_on_payment = request.args.get("late_on_payment")
    age = request.args.get("age")
    years_in_contract = request.args.get("years_in_contract")
    request_data = [[is_male, num_inters, late_on_payment, age, years_in_contract]]

    return str(MODEL.predict(request_data)[0])


# Running from pycharm the code instead of terminal
if __name__ == "__main__":
    app.run(host='0.0.0.0')

