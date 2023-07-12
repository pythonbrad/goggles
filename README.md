[LOHCE Careathon 2023](https://github.com/lohce/careathon2023)


Dependencies
===

Build dependencies
---
- [Flask](https://flask.palletsprojects.com/en/2.3.x)

Runtime dependencies
---
- [FFMPEG](https://ffmpeg.org)
- [Vosk](https://alphacephei.com/vosk/install)
- [gTTS](https://gtts.readthedocs.io/en/latest)


Usage
===

Installation
---

In using Pip
```sh
pip3 install -r requirements.txt
```

In using Pipenv
```sh
pip3 install pipenv
pipenv install
```

Execution
---

Execute the command below, and enter [http://127.0.0.1:2006](http://127.0.0.1:2006) in you web browser.
```sh
python runserver.py -p 2006
```

Translation
---

The translation can be edited via the [vocal_assistant/languages.py](vocal_assistant/languages.py) file.
Current just two languages are supported (French and English).
