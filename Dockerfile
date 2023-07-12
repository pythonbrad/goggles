FROM python:3.11

WORKDIR /python-docker

RUN wget https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v4.4.1/ffmpeg-4.4.1-linux-32.zip
RUN unzip ffmpeg-4.4.1-linux-32.zip && rm ffmpeg-4.4.1-linux-32.zip
RUN chmod 755 ffmpeg
ENV PATH="$PATH:."

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "runserver.py" ]