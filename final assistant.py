import pyttsx3
import wikipedia
import pyaudio
import pywhatkit
import datetime
import speech_recognition as sr
In=pyttsx3.init()
listener=sr.Recognizer()
def talk(text):
    In.say(text)
    In.runAndWait()
def inputinst():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            audio=listener.listen(origin)
            instruction=listener.recognize_google(audio)
            print(instruction)
            
    except:
        pass   
    return instruction
def play():    
    instruction=inputinst()
    print(instruction)        
    if "play" in instruction:
         song=instruction.replace("play","")
         talk("playing"+song)
         pywhatkit.playonyt(song)
    elif "time" in instruction:
        time=datetime.datetime.now().strftime("%I:%M%p")
        talk("current time"+time)
    elif "date" in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date"+date)
    elif"how are you" in instruction:
        talk("I am good")
    elif"what is your name" in instruction:
        talk("I am doremon,what can I do for u ?")
    elif"who is" in instruction:
        human=instruction.replace("who is"," ")
        info=wikipedia.summary(human,sentences=2)
        print(info)
        talk(info)
    else:
        talk("please repeat")

play()