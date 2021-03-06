# Earth Hz
User-friendly web framework for sharing and collaborative labeling of bioacoustic data.

## Features
* Imports raw WAV files from audio recorders uploaded to cloud storage (currently supports Azure Data Lake)
* Generates MP3 or Ogg stream on the fly, supports playback in any HTML5 compatible browser
* Imports cluster files from Wildlife Acoustics Kaleidoscope 

## Installation
```bash
apt-get install ffmpeg libavcodec-extra
pip install -r requirements.txt
```

## Running
Run on a local machine for single user / testing
```bash
flask run
```
### Or
See https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/ and https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux for suggestions on deploying to a production server.

## Framework
* [Flask](http://flask.pocoo.org/)
