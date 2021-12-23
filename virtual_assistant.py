import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import PyPDF2
import pdfplumber
import cv2
import pyjokes
import webbrowser
import spotify

#webbrowser.open_new('https://www.google.com/')


listener = sr.Recognizer()


#engine.say("Hi!Sayani I am your bot henry")
#engine.say("How can I help you?")




def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',150 )
    engine.setProperty('voice', voices[0].id)
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()
    
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('Start speaking please.')
            talk('Start speaking please.')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'henry' in command:
                command = command.replace('henry', '')
                print(command)
    except:
        pass
    if command == '':
        command = "ok"
    return command
    
def run_henry():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Ok I am playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'spotify' in command:
        playlist = command.replace('spotify', '')
    
    elif 'read' in command :
        book=open('advs.pdf','rb')
        PdfReader=PyPDF2.PdfFileReader(book)
        Pages= PdfReader.numPages
        for i in range(Pages):
            page = PdfReader.getPage(i)
            content=page.extractText()
            print(content)
        
            print(Pages)
            talk(content)
   
    elif 'camera' in command:
        cap=cv2.VideoCapture(0) 
        cap.set(3,1280)
        while(True):
            d,img=cap.read()
            img=cv2.flip(img, 1)
            cv2.imshow('demo',img)
            if cv2.waitKey(1)==ord('a'):
                break
        cap.release()
        cv2.destroyAllWindows()        
    
    elif 'google' in command:
        web =  webbrowser.open_new('https://www.google.com/')
        talk('ok i am opening google!')
        
    elif 'youtube' in command:
        web = webbrowser.open_new('https://www.youtube.com/')
        talk('sure! I am opening youtube')
          
        
    elif 'joke' in command:
        jokes=command.replace('jokes','')
        joke=pyjokes.get_joke()
        print(joke)
        talk('ok!' + joke)
      
        
    elif 'who is' in command:
        person = command.replace('who is','')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)    
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print(time)
    
    elif 'hello' in command:
        talk('Hi!')
        
    elif 'good morning' in command:
        talk('good morning sayani')
        
    elif 'good night' in command:
        talk('good night sayani!sweet dreams')
        
    elif 'who made you' in command:
        talk('Ms.Sayani Ghatak made me')
        
    elif 'how are you' in command:
        talk('I am fine!Thank you for asking!')
        
    elif 'bye' in command:
        talk('bye!')
        quit()
        
    else:
        talk('Please say  again .I can not understand what you want to say!')
while True:
    talk("Hi!Sayani I am your bot henry How can I help you?")
    run_henry()