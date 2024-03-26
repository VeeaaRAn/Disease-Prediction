# utils.py
from werkzeug.utils import secure_filename
import os

def save(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join('static/upload', filename)
    file.save(file_path)
    return file_path

