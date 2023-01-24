
from flask import Flask
from flask import request,jsonify
from flask_cors import CORS
import os
import io
import soundfile
from audio_tools import audiotools
from db import users
from utils import hashing
db=users.Users()
at=audiotools.AudioTools()
app = Flask(__name__)
CORS(app)

@app.post("/isuser")
def isuser():
    username=request.form['username']
    response=None
    if(db.isUser(username)):
        response = jsonify("TRUE") 
    else:
        response = jsonify("FALSE")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.post("/register")
def register():
    files = request.files
    file=files.get('file')
    username=request.form['username']
    password=hashing.genhash()
    res=db.newUser(username,password)
    os.chdir("audiodb/")
    filepath = os.path.join("{}.wav".format(password))
    file.save(filepath)
    file.seek(0)
    data, samplerate = soundfile.read(file)
    with io.BytesIO() as fio:
        soundfile.write(
            fio, 
            data, 
            samplerate=samplerate, 
            subtype='PCM_16', 
            format='wav'
        )
        data = fio.getvalue()
    print('voice registered for ',username)
    response = jsonify("DONE")
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.post("/login")
def login():
    files = request.files
    file=files.get('file')
    username=request.form['username']
    # Write the data to a file.
    os.chdir("audiodb")
    filepath = os.path.join("received.wav")
    file.save(filepath)

    # Jump back to the beginning of the file.
    file.seek(0)
    # Read the audio data again.
    data, samplerate = soundfile.read(file)
    with io.BytesIO() as fio:
        soundfile.write(
            fio, 
            data, 
            samplerate=samplerate, 
            subtype='PCM_16', 
            format='wav'
        )
        data = fio.getvalue()
    hash=db.getUserHash(username)
    result=at.identify(hash)
    response=None
    if(result):
        print('Access granted to ',username)
        response = jsonify("SUCCESS")
    else:
        response = jsonify("FAIL")
    
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response