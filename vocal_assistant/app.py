from flask import (
    Flask, redirect, request, render_template, send_file, session, url_for)
import io
from .languages import ui_languages, voice_languages
import tempfile
from . import vocal_api
import random


app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/toggle_language")
def toggle_language():
    language = session.get("language", None)

    session['language'] = 'fr' if language == 'en' else 'en'

    return redirect(url_for('index'))


@app.route("/")
def index():
    language = session.get('language', 'en')

    return render_template(
        "index.html",
        id=random.random(),
        **ui_languages[language],
    )


@app.route("/listen", methods=["POST"])
def listen():
    language = session.get('language', 'en')

    if not request.files:
        message = random.choice(
            voice_languages[language]['dont_hear'])
    else:
        upload = request.files['file']
        _type, ext = upload.mimetype.split('/')

        if _type != 'audio':
            message = random.choice(
                voice_languages[language]['dont_hear'])
        else:
            tmp = tempfile.NamedTemporaryFile()
            tmp.close()

            destination = f"{tmp.name}.{ext}"

            upload.save(destination)

            status, message = vocal_api.transcribe(
                destination, language)

            if not status:
                message = random.choice(
                    voice_languages[language]['dont_understand'])

    session['message'] = message

    return {
        'result': f"{url_for('speak')}?id={random.random()}",
        'type': 'audio/mp3'
    }


@app.route("/speak", methods=["GET"])
def speak():
    language = session.get('language', 'en')

    if 'message' in session:
        message = session.pop('message')
    else:
        message = random.choice(voice_languages[language]['welcome'])

    status, audio = vocal_api.speech(message, language)

    if not status:
        with open(f'vocal_assistant/data/error_{language}.mp3', 'rb') as f:
            audio = f.read()

    return send_file(
        io.BytesIO(audio),
        mimetype='audio/mp3',
    )
