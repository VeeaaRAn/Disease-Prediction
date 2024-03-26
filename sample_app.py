from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=["*"])
@app.route('/')
def index():
    return render_template('sample.html')
@app.route('/sample',methods=['POST'])
def sample():
    if request.method== 'POST':
        message=request.get_json()
        name=message['name']
    response={
        'greeting':name +  " Welcome to our website!"
    }
    return  jsonify(response)

if  __name__ == "__main__":
    app.run()