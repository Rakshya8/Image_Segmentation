from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder='pages')

# Set the secret key
app.secret_key = 'aisdaio1023029'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Generate a secure filename and save the file
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            flash('File successfully uploaded')
            # Store the file path in a variable
            file_location = file_path
            # Use the file_location variable as needed
            print("File location:", file_location)
            return redirect(request.url)
        else:
            flash('Allowed file types are png, jpg, jpeg')
            return redirect(request.url)
    # For GET requests, simply return the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
