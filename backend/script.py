
from flask import Flask
from flask import request,jsonify
from flask_cors import CORS
import os
import io
import soundfile
from audio_tools import audiotools
at=audiotools.AudioTools()
# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_wav("./processed1.wav")
# sound.export("transcript.wav", format="wav")


# # transcribe audio file                                                         
# AUDIO_FILE = "transcript.wav"

# # use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file                  

#         print("Transcription: " + r.recognize_google(audio))


app = Flask(__name__)
CORS(app)

@app.post("/isuser")
def isuser():
    username=request.form['username']
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    response=None
    if(f'{username}.wav' in files):
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
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # Write the data to a file.
    filepath = os.path.join("{}.wav".format(username))
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
    result=at.identify(username)
    response=None
    if(result):
        print('Access granted to ',username)
        response = jsonify("SUCCESS")
    else:
        response = jsonify("FAIL")
    
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response