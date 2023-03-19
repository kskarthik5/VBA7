import speech_recognition as sr
import os
from pydub import AudioSegment
from speechbrain.pretrained import SpeakerRecognition
class AudioTools:
    def __init__(self):
        self.verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
        self.sr = sr.Recognizer()

    def transcript(self):                       
        AUDIO_FILE = "received.wav"                        
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = self.sr.record(source)  # read the entire audio file                  

                return self.sr.recognize_google(audio)

    def identify(self,username):
        score, prediction = self.verification.verify_files("received.wav", "{}.wav".format(username))
        return prediction[0]
