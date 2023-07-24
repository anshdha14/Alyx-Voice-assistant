import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hi i am alyx, how can i help you")

def takeCommand():
#takes microphone input and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f,"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    speak("how are you")
    takeCommand()
