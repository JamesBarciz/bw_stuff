import random

import pandas as pd

from flask import Flask

app = Flask(__name__)
data = pd.read_csv('data/live_data.csv')


@app.route('/')
def base():
    return 'This is a basic Flask application.'


@app.route('/data')
def display_data():
    return data.to_json()


@app.route('/predict')
def predict():
    return data.iloc[random.randint(0, len(data) - 1)].to_json()


if __name__ == '__main__':
    app.run()
