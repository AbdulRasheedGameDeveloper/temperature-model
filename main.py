import pickle
from flask import Flask, render_template, request
from numpy import outer

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])

def predict():
    prediction = model.predict([[request.form.get('temperature')]])
    output = round(prediction[0], 2)
    print(output)
    return render_template('index.html', prediction_text=f'Total Revenue You Can Except is Rs. {output}/-')

if __name__=='__main__':
    app.run(debug=True)