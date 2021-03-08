import speech_recognition as sr
# to listen from user
import wikipedia
# to srch stuffs on internet
import pyjokes
# to listen random joke
import pyttsx3
# to computer to speek
import pywhatkit
import datetime
listner =sr.Recognizer()
engine=pyttsx3.init()

#alexa will talk through this function

def talk(text):
 engine.say(text)
 engine.runAndWait()


# to take commands from user
def  take_command():
  try:
    with sr.Microphone() as source:
       print('listening...')
       voice=listner.listen(source)
       command=listner.recognize_google(voice)
       command=command.lower()
       if 'alexa' in command:
           command=command.replace('alexa','')
           print(command)
  except:

      pass
  return command

def run():
    cmd=take_command()
    print(cmd)

    if 'play' in cmd:
        song=cmd.replace('play','')

        talk('playing'+ song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in cmd:
       time=datetime.datetime.now().strftime('%I:%M %p')
       talk('current time is '+time)
    elif 'who is' or 'tell me' in cmd:
      person=cmd.replace('who is ','')
      info=wikipedia.summary(person,1)

      print(info)
      talk(info)

    elif 'joke' in cmd:
        talk(pyjokes.get_joke())
    else:
        talk('pardon plese repeat command')

while True:

 run()