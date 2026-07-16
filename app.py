from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

models = {
    'Maruti': pickle.load(open('Maruti.pkl', 'rb')),
    'Hyundai': pickle.load(open('Hyundai.pkl', 'rb')),
    'Mahindra': pickle.load(open('Mahindra.pkl', 'rb')),
    'Tata': pickle.load(open('Tata.pkl', 'rb')),
    'Honda': pickle.load(open('Honda.pkl', 'rb'))
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    brand = request.form['brand']
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    fuel = int(request.form['fuel'])
    seller_type = int(request.form['seller_type'])
    transmission = int(request.form['transmission'])
    owner = int(request.form['owner'])

    model = models[brand]
    prediction = model.predict([[year, km_driven, fuel, seller_type, transmission, owner]])
    price = round(prediction[0], 2)

    return render_template('index.html', prediction=f'₹ {price}')

if __name__ == '__main__':
    app.run(debug=True)