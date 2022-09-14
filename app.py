from flask import Flask, request, render_template

from artifacts.utiles import dum

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('wine.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.form
    predict_object = dum(data)
    result  = predict_object.predict()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
