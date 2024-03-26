




# app.py
from flask import Flask, render_template, request
from classifier import classify
from saving import save
from solution import solution
import logging

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload'
model_path = 'Model.h5'  # Replace with the actual path to your model file
classifier = classify(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class = None
    file_path = None
    L=None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                file_path = save(file)
                predicted_class = classifier.predict(file_path)
                print(predicted_class)
            except Exception as e:
                print(f"Error predicting class for image: {e}")
                return render_template('index.html', filename=None, predicted_class="Error predicting class")
        print(predicted_class)
        new=solution(predicted_class)
        suggestion=new.fertilizer(predicted_class)
    return render_template('index.html', filename=file_path, predicted_class=predicted_class,suggestion=suggestion,hello='hello')

if __name__ == '__main__':
    app.run(debug=True)



# app.py
from flask import Flask, render_template, request
from classifier import classify
from saving import save
from solution import solution
import logging
from django.shortcuts import render


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload'
model_path = 'Model.h5'  # Replace with the actual path to your model file
classifier = classify(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class = None
    file_path = None
    L=None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                file_path = save(file)
                predicted_class = classifier.predict(file_path)
                
            except Exception as e:
                print(f"Error predicting class for image: {e}")
                return render_template('index.html', filename=None, predicted_class="Error predicting class")
    pred=str(predicted_class)
    new=solution(pred)
    suggestion=new.fertilizer(pred)
    context = {
            'filename': file_path,
            'predicted_class': predicted_class,
            'suggest' : suggestion, 
            'test' : "testing"
            # Other context variables
        }
    return render(request, 'index.html', context)


if __name__ == '_main_':
    app.run(debug=True)
