from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def start_upload():
    if request.method == 'POST':
        screen_address = request.form["screen"]
        file = request.files['file']
        file.save(secure_filename(file.filename))
    else:
        return render_template('upload.html')

    print(screen_address)
    print(file)
    return 'uploading to screenly'

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()