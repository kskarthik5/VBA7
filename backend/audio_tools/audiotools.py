import speech_recognition as sr
from os import path
from pydub import AudioSegment
from speechbrain.pretrained import SpeakerRecognition
class AudioTools:
    def __init__(self):
        self.verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")

    def recognize(self):
        # convert mp3 file to wav                                                       
        sound = AudioSegment.from_wav("./processed1.wav")
        sound.export("transcript.wav", format="wav")


        # transcribe audio file                                                         
        AUDIO_FILE = "transcript.wav"

        # use the audio file as the audio source                                        
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file                  

                print("Transcription: " + r.recognize_google(audio))

    def identify(self,username):
        score, prediction = self.verification.verify_files("received.wav", "{}.wav".format(username))
        print(prediction, score)
        return prediction[0]
