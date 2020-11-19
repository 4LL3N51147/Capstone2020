import imghdr
import subprocess
import os
import time
from flask import Flask, render_template, request, redirect, url_for, abort, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpeg', '.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

def cloak_image(mode):
    bashCommand = "python ./fawkes/protection.py -d {} -m {}".format("./uploads", mode)
    process = subprocess.run(bashCommand, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    print(process)

@app.route('/yield')
def yieldRoute():
    def inner():
        proc = subprocess.Popen(
            ['dmesg'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return Response(inner(), mimetype='text/html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    selected_mode = request.form['mode']
    file_full = secure_filename(uploaded_file.filename)
    if file_full != '':
        file_name, file_ext = os.path.splitext(file_full)
        file_name += "_{}".format(selected_mode)
        print(file_name, file_ext)
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "unsupported file format"
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], file_name+file_ext))
        cloak_image(selected_mode)
    return redirect(url_for('index'))

app.run()