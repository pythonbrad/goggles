import subprocess


def transcribe(filename, language) -> (bool, str):
    process = subprocess.Popen([
        'vosk-transcriber', '-i', filename,
        '-l', language
    ], stdout=subprocess.PIPE)

    out = process.communicate()[0].decode("ISO-8859-1")
    success = process.returncode == 0

    return success, out


def speech(text, language) -> (bool, bytes):
    process = subprocess.Popen(
        ['gtts-cli', text.encode('utf-8'), '-l', language],
        stdout=subprocess.PIPE)

    out = process.communicate()[0]
    success = process.returncode == 0

    return success, out
