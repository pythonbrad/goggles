#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from vocal_assistant.app import app

parser = argparse.ArgumentParser(description="Vocal Assistant")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=2006,
)
args = parser.parse_args()

if __name__ == '__main__':
    flask_options = dict(
        host='0.0.0.0',
        debug=True,
        port=args.port,
        threaded=True,
    )

    app.run(**flask_options)
