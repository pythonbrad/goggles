import subprocess


def transcribe(filename, language) -> (bool, str):
    process = subprocess.Popen([
        'vosk-transcriber', '-i', filename,
        '-l', language
    ], stdout=subprocess.PIPE)

    out = process.communicate()[0].decode("ISO-8859-1")
    status = process.returncode == 0

    return status, out


def speech(text, language) -> (bool, bytes):
    process = subprocess.Popen(
        ['gtts-cli', text.encode('utf-8'), '-l', language],
        stdout=subprocess.PIPE)

    out = process.communicate()[0]
    status = process.returncode == 0

    return status, out
