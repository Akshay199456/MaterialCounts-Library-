import os

from flask import Flask, render_template, request

# Importing OCR function from ocr_core.py
from ocr_core import ocr_core

# Defining a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# Allowing files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])

app = Flask(__name__)

# Function to check the file extension
def allowed_file(filename):
	return '.' in filename \
			and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route and function to handle the home page
@app.route('/')
def home_page():
	return render_template('index.html')

# Route and function to handle the upload page
@app.route('/upload', methods = ['GET',  'POST'])
def upload_page():
	if(request.method == 'POST'):
		# Check if there is a file in the request
		if 'file' not in request.files:
			return render_template('upload.html', msg = 'No  file selected')
		file = request.files['file']

		# If no file is selected
		if file.filename == '':
			return render_template('upload.html', msg = 'No file selected')

		if file and allowed_file(file.filename):

			# Call the OCR function on it
			extracted_text = ocr_core(file)

			#  Extract the text and display it
			return render_template('upload.html',
									msg = 'Successfully processed',
									extracted_text  = extracted_text,
									img_src = UPLOAD_FOLDER + file.filename)

	elif request.method == 'GET':
		return render_template('upload.html')

if(__name__ == '__main__'):
	app.run()