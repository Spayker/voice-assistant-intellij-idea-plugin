import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


# main functions section
def speak(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")


def record_audio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print "Say Something"
        audio = r.listen(source)

        # Speech recognition using Google API
        data = ""
        try:
            # Uses the default API key
            data = r.recognize_google(audio)
            print "You said" + data
        except sr.UnknownValueError:
            print "Google API could not recognize audio"
        except sr.RequestError as e:
            print "Could not get results from Google API service: {0}".format(e)

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is. ")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# main functions end section

# init section
time.sleep(2)
speak("Hi Alex, what can I do for you?")
while 1:
    data = record_audio()
    jarvis(data)

# init section end
