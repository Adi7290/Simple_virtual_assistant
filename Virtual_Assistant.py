import pyttsx3
import speech_recognition as sr

def take_commands():
    #Making the use of Recognizer and microphone
    #method for speech_Recognition
    #For Taking commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        #Now Seconds before not speaaking
        #a phrase is considered complete
        r.pause_threshold=0.7
        audio = r.listen(source)

        try:
            print('Recognizing')
            #for listening the command indian english
            Query= r.recognize_google(audio,language='en-in')
        except Exception as e:
            #Exception handling method
            #also used for asking the commmand again
            print(e)
            print('Error occured say that again')
            return "none"
    return Query

def Speak(audio):
    #intialize pyttsx3
    engine = pyttsx3.init()
    #getter and setter method
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

if __name__=='__main__':
    while True:
        command = take_commands()
        if "exit" in command:
            print('Okay see you later bye')
