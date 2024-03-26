# app.py
from flask import Flask, render_template, request
from classifier import classify
from saving import save
from solution import solution
import logging
test=[]
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload'
model_path = 'Model.h5'  # Replace with the actual path to your model file
classifier = classify(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class = None
    file_path = None
    suggestion=None

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
        elem=suggestion.split('.')
        for i in elem:
            test.append(i)
            
            
    return render_template('index.html', filename=file_path, predicted_class=predicted_class,suggest=test)

if __name__ == '__main__':
    app.run(debug=True)