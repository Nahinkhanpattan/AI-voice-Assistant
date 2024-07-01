import pyttsx3
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import speech_recognition as sr

engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(command):
    print("Speaking:", command)  # Debugging line
    engine.say(command)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("good afternoon sir!")
    elif hour >=18 and hour <24:
        speak("good evening sir!")
    else:
        speak("good night sir!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)

    except Exception as e:
        print(e)
        speak("Say that again...")
        return "none"
    return query

def sendEmail(to,content):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("nahinkirito@gmail.com","ovuajuplrnmssbhj")
        server.sendmail("nahinkirito@gmail.com",to,content)
        server.close()

def open_in_browser(search):
    chromepath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    wb.register('brave', None, wb.BackgroundBrowser(chromepath))
    wb.get('brave').open_new_tab(search + ".com")

def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\INFINIX\\Desktop\\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(str(battery.percent)+"percent")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("searching.....") 
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="suneethajeldi@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send the mail")
        elif "open in chrome" in query:
            speak("what should i open in chrome")
            search=takecommand().lower()
            open_in_browser(search)
        elif "logout" in query:
            os.system("shutdown /l")
        elif "restart" in query:
            os.system("shutdown /r /t 1")   
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "play songs" in query:
            songs_dr="C:\\Users\\INFINIX\\Downloads\\songs"
            songs=os.listdir(songs_dr)
            os.startfile(os.path.join(songs_dr,songs[0]))
        elif "remember this" in query:
            speak("what should i remember")
            data=takecommand()
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "did you remember anything" in query:
            remember=open('data.txt','r')
            speak("you told me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        elif "offline" in query:
            quit()
            