import pyttsx3
import speech_recognition as sr
# import torch
# import torchaudio
# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


engine = pyttsx3.init()
voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice', voices[1].id)


# Text to Speech Function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def Input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_sphinx(audio, language="en-US")
        # query = query.lower()
        # if "luna" in query:
        print(f"user said: {query}")    

    except Exception as e:
        speak("Could you say that again please...")
    return None
        


if __name__ == "__main__":
    speak("This is a test.")
    # Input()    