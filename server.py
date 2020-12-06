import imghdr
import subprocess
import os
import time
import secrets 
import string
import pathlib
from flask import Flask, render_template, request, redirect, url_for, abort, Response, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpeg', '.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

def genSecretToken(N=16): 
	res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
	return str(res)

def validate_image(stream):
	header = stream.read(512)
	stream.seek(0) 
	format = imghdr.what(None, header)
	if not format:
		return None
	return '.' + (format if format != 'jpeg' else 'jpg')

def cloak_image(path, mode):
	bashCommand = ["python", "./fawkes/protection.py", "-d", os.path.join(app.config['UPLOAD_PATH'], path), "-m", str(mode)]
	process = subprocess.Popen(bashCommand)
	return process.wait()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
	token = genSecretToken()
	print(token)
	print(request)
	uploaded_file = request.files['file']
	selected_mode = request.form['mode']
	file_full = secure_filename(uploaded_file.filename)
	if file_full != '':
		file_name, file_ext = os.path.splitext(file_full)
		if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
				file_ext != validate_image(uploaded_file.stream):
			return "unsupported file format"
		pathlib.Path(app.config['UPLOAD_PATH'], token).mkdir(exist_ok=True)
		uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], token, file_name+file_ext))
		cloak_image(token, selected_mode)
	else:
		return redirect(url_for("index"))

	cloaked_image_path = os.path.join(app.config['UPLOAD_PATH'], token, file_name+"_{}_cloaked.png".format(selected_mode))
	if os.path.exists(cloaked_image_path):
		return send_file(cloaked_image_path)
	else:
		return cloaked_image_path

app.run()