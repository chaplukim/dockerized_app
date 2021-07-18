import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request

def test_model_loading(x_test_file, y_pred_file, my_model):
    """Checks if the files are loaded correctly"""
    x_test = pd.read_csv(x_test_file)
    y_pred = np.loadtxt(y_pred_file)

    # Repredict the y_pred:
    new_pred = my_model.predict(x_test)

    # compare:
    for idx in range(len(new_pred)):
        if y_pred[idx] == new_pred[idx]:
            continue
        else:
            print(f"Issue within prediction no {idx}")
            return ""
    print("Function Test: Model pickle loading ok")


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


# the name of the app(flask()):
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route("/predict_churn", methods=["GET"])
def get_prediction():
    result = 0
    is_male = request.args.get("is_male")
    num_inters = request.args.get("num_inters")
    late_on_payment = request.args.get("late_on_payment")
    age = request.args.get("age")
    years_in_contract = request.args.get("years_in_contract")
    request_data = [[is_male, num_inters, late_on_payment, age, years_in_contract]]

    return str(model.predict(request_data)[0])


# Running from pycharm the code instead of terminal
if __name__ == "__main__":
    with open("churn_model.pkl", "rb") as pf:
        model = pickle.load(pf)
    test_model_loading("x_test.csv", "preds.csv", model)

    app.run()

print("end of inference")