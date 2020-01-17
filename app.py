import os

from flask import Flask, render_template, request
# Importing OCR function from ocr_core.py
from ocr_core import ocr_core
# Importing secure_filename
from werkzeug.utils import secure_filename



APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print('Application root: ', APP_ROOT)

# Defining a folder to store and later serve the images
UPLOAD_LOCATION = '/uploads'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_LOCATION)

# Allowing files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

			# Secures filename before storing it in the system
			filename = secure_filename(file.filename)
			print("File path: ", os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			#  Extract the text and display it
			return render_template('upload.html',
									msg = 'Successfully processed',
									extracted_text  = extracted_text,
									img_src = UPLOAD_FOLDER + file.filename)

	elif request.method == 'GET':
		return render_template('upload.html')

if(__name__ == '__main__'):
	app.run()