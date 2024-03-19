from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
import secrets
from waitress import serve
from Speech_to_Text import *
from Summarizer import summarize_text
from Sender import send_mail
from Template import *
from Translator import *

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile("config.cfg")

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
filename = ""

@app.route('/')
def home():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSION']


@app.route('/upload', methods=['POST'])
async def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No file is choosen'
    
    if file and allowed_file(file.filename):
        global filename
        filename = secure_filename(file.filename)
        folder = os.path.join(app.instance_path, 'temp')
        os.makedirs(folder, exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload', filenam=filename))
    
    else:
        return '<h2>Invalid File Format.</h2>'

@app.route('/process/<filenam>', methods=['GET', 'POST'])
def upload(filenam):
    if request.method == 'POST':
        print(request.form)
        category = request.form['cat']
        context = request.form.get('textarea')
        endft = request.form.get('topic')
        mail = request.form.get('mail')
        lang = request.form.get('lang')
        print(filenam, context, category, endft, lang)
        if filenam == '<filenam>':
            filenam = filename
        
        result = process_file(filenam, mail, lang, context, category, endft)
        return render_template('final.html', summary=result)
    return render_template('upload.html', category = audio_prompts, language = sorted(LANGUAGES.values()))

@app.route("/report", methods=["GET"])
def process_file(filepath, mail, lang, context='some topic', category='transcript', endft='dates and palces'):
    y = ''
    if not mail:
        mail = '210303105522@paruluniversity.ac.in'

    for i in app.config['ALLOWED_EXTENSION']:
        if filepath.endswith(i):
            y = i
            break

    if y == 'txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            file = f.read()
    
    elif y=='mp4':
        file = ''

    else:
        file = generate_transcript(filepath)

    if not lang:
        lang = 'english'
    summary = summarize_text(file, topic=context, category=category, endft=endft)
    try:
        summary = translates(summary, lang)
    except Exception as e:
        print('Could not translate',e )

    try:
        send_mail([mail], 'temp', summary)
    except:
        pass

    return summary

    
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=80)


