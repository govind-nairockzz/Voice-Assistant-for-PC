import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import re
import cv2
import subprocess
import smtplib
import pyowm

##################################################################################DATA-SET####################################################################################################################################################################################################################################################################################
greetings = ['hey there','hello','hey']
greet=['hey there ']
question = ['how are you', 'how are you doing']
responses = ["I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['It is a classified information.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video','youtube']
cmd5 = ['tell me the weather', 'weather', 'what about the weather','how is the weather','tell me the weather']
cmd6 = ['exit', 'close', 'goodbye', 'terminate','abort','close this'.'exit this','abort the voice assistant','abort the va']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['right now its rainbow', 'right now its transparent', 'right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']
cmd10=['open microsoft word','open word','ms word','open ms word','start ms word']
cmd11=['open ms excel','ms excel','excel','start excel']
cmd12=['ms acess','acess','open ms acess','start ms acess']
cmd13=['power point','open ms power point','microsoft power point','start ms powerpoint','open power point']
cmd14=['take photo','photo','take picture','take a snap','click me a photo','take a photo']

###############################################################################VOICE-MODULATION#######################################################################################################################################################################################################################################################################################


voices=[]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#########################VOICE-PROCESS#################################

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#########################Greetings from Veronica################################

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon")   

    else:
        print("Good Evening!")
        speak("Good Evening")  
    print("I am Veronica Sir how may I help you")
    speak("I am Veronica Sir how may I help you")       

######################Veronica VOICE-INPUT MODULE#######################################

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.energy_threshold = 4000
        r.pause_threshold=1
        audio = r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    try:
        print("Recognizing......")    
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

##############################[VERONICA ->MAIN FUNCTION]############################################

if __name__ == "__main__":
    wishMe()
    print("Say exit or goodbye to exit")
    while True:
    # if 1:
        query = takeCommand().lower()
        if query in greetings:
            print(greet[0])
            speak(greet)
            engine.runAndWait()

        elif query in question :
            speak(responses)
            print(responses)
            engine.runAndWait()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Govind Nair\\Desktop\\ss.py"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
                    

               
        elif query in var1:
            speak('Sorry Acess denied')
            engine.runAndWait()
            reply = random.choice(var2)
            print(reply)
               
        elif query in var3:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif query in var4:
            speak('I am Veronica ')
            print('I am Veronica')
            engine.runAndWait()
                       
		
        elif query in cmd1:
            webbrowser.open('www.google.com')
		
        elif query in cmd2:
            music_dir = 'C:\\Users\\Govind Nair\\Music'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif query in cmd3:
            jokrep = random.choice(jokes)
            speak(jokrep)
            engine.runAndWait()
		
        elif query in cmd4:
            webbrowser.open('www.youtube.com')
		
        elif query in cmd5:
            reg_ex = re.search('current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))

		
        elif query in cmd6:
            print('see you later')
            speak('see you later')
            engine.runAndWait()
            exit()
			
	
        elif query in cmd7:
            print(random.choice(colrep))
            speak(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            speak('It keeps changing every micro second')
               
               
        elif query in cmd8:
            print(random.choice(colrep))
            speak(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            speak('It keeps changing every micro second')
               
        elif query in cmd9:
            print(random.choice(repfr9))
            speak(random.choice(repfr9))
            engine.runAndWait()               

        elif query in cmd10:
            print('opening MS word')
            os.startfile('WINWORD.EXE')
		
        elif query in cmd11:
            print('opening MS EXCEL')
            os.startfile('EXCEL.EXE')
		
        elif query in cmd12:
            print('opening MS Acess')
            os.startfile('MSACCESS.EXE')
			
        elif query in cmd13:
            print('opening MS Power Point')
            os.startfile('POWERPNT.EXE')

        elif query in cmd14:
                camera = cv2.VideoCapture(0)
                for i in range(1):
                    return_value, image = camera.read()
                    cv2.imwrite('opencv'+str(i)+'.png', image)
                del(camera)

			
		

			







			   
		


