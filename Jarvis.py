import datetime
import smtplib
from pprint import pprint

import webbrowser
import random
import pyttsx3
import speech_recognition as sr
import requests


engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Working on it...")
        query = r.recognize_google(audio, language='iw-IL')
        print(f"Boss asked:{query}\n")

    except Exception as e:
        print(e)
        print("_")
        speak("")
        return "None"
    return query

Facts = ["Hunting unicorns is legal in Michigan", "Someone actually paid $10,000 for invisible artwork", "There's an American town with a population of one."]

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'עדכון' in query:
            strTime = datetime.datetime.now().strftime("%I hours ")
            strTime2 = datetime.datetime.now().strftime("and:%M minutes.")
            speak(f"Sir, the time is {strTime}")
            speak(f"{strTime2}")
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'תן לי עדכון' in query:
            strTime = datetime.datetime.now().strftime("%I hours ")
            strTime2 = datetime.datetime.now().strftime("and:%M minutes.")
            speak(f"Sir, the time is {strTime}")
            speak(f"{strTime2}")
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'מה חדש' in query:
            url = "https://www.google.com/search?q=%D7%97%D7%93%D7%A9%D7%95%D7%AA&oq=%D7%97%D7%93%D7%A9&aqs=chrome.0.0i131i433i457j69i57j0j0i131i433j0l3j0i395.2818j1j7&sourceid=chrome&ie=UTF-8"
            webbrowser.get().open(url)
            speak("These are the top new news in Israel.")

        elif 'שלום' in query:
            speak("Hello.")

        elif 'עץ או פלי' in query:
            moves=["Pali", "Etz"]
            cmove=random.choice(moves)
            speak("The computer chose. " + cmove)

        elif 'מהו מזג האוויר' in query:
            url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59j0l7.2446j0j9&sourceid=chrome&ie=UTF-8"
            webbrowser.get().open(url)
            speak("Here is what I found on google for your current location.")

        elif 'איך מזג האוויר' in query:
            url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59j0l7.2446j0j9&sourceid=chrome&ie=UTF-8"
            webbrowser.get().open(url)
            speak("Here is what I found on google for your current location.")

        elif 'מי יצר אותך' in query:
            speak('My boss made me. His name is Ariel.')

        elif 'מה השעה' in query:
            strTime = datetime.datetime.now().strftime("%I and:%M, sir.")
            speak(f"It's {strTime}")

        elif 'איך קוראים לך' in query:
            speak('My name is Jarvis.')

        elif 'מה השם שלך' in query:    
            speak('My name is, Jarvis.')
        
        elif '.' in query:
            speak('It works')

        elif 'חפש משהו בויקיפדיה' in query:
            speak('what should I search?')
            query = takeCommand().lower()
            url = ('https://en.wikipedia.org/wiki/'+query)
            webbrowser.get().open(url)
            speak("okay. That's what I have found for " + query) 

        elif "איפה אני" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You are somewhere near here, acording to Google maps.") 

        elif "איפה אני נמצא" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You are somewhere near here, acording to Google maps.") 

        elif "איפה אני נמצאת" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You are somewhere near here, acording to Google maps.") 

        elif 'תתחיל ספירה לאחור' in query:
            speak("For how many seconds?")
            query = takeCommand().lower()
            num1 = int(query)
            while num1 > 0:
                speak(num1)
                num1 = num1 - 1

        elif 'פתח שעון' in query:
            speak("For how many seconds?")
            query = takeCommand().lower()
            num1 = int(query)
            while num1 > 0:
                speak(num1)
                num1 = num1 - 1

        elif "תודה" in query:
            speak("Youre welcome boss.")
        
        elif 'שים משהו ביוטיוב' in query:
            speak('what should I type?')
            query = takeCommand().lower()
            url = "https://www.youtube.com/results?search_query=" + query
            webbrowser.get().open(url)
            speak("Have fun sir.")

        elif 'שים מוזיקה' in query:
            speak('should I open youtube?')
            if takeCommand().lower() == "yes":
                speak('what should I type?')
                query = takeCommand().lower()
                url = "https://www.youtube.com/results?search_query=" + query
                webbrowser.get().open(url)
                speak("Have fun sir.")
            else:
                speak("okay boss, I'm here if you need me.")
        
        elif 'חפש משהו בגוגל' in query:
            speak('what should I search?')
            query = takeCommand().lower()
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
            speak("Here is what I found on google.")

        elif 'למד אותי משהו חדש' in query:
            speak(random.choice(Facts))

        elif 'ספר לי משהו מעניין' in query:
            speak(random.choice(Facts))
        
        elif 'מי זה' in query:
            speak('I am jarvis. I am a virtual assistant.')
        
        elif 'מי אתה' in query:
            speak('I am Jarvis. I am a virtual assistant.')

        elif 'אבחון מערכות' in query:
            speak('Check!')

        elif 'מה שלומך' in query:
            speak("Just fine sir. How are you?")

        elif 'מה נשמע' in query:
            speak('I am fine sir. Thank you for asking.')
        
        elif 'ספר לי בדיחה' in query:
            speak('Why did the chicken cross the road. to get to the other side.')
        
        elif 'תגיד שלום' in query:
            speak('Hello. I am Jarvis. A virtual assistant.')

        #MATH -START-

        elif there_exists(["פלוס","ועוד","+"]):
            opr = query.split()[1]
            speak(int(query.split()[0]) + int(query.split()[2]))

        elif there_exists(["פחות","מינוס","-"]):
            opr = query.split()[1]
            speak(int(query.split()[0]) - int(query.split()[2]))

        elif there_exists(["כפול","*"]):
            opr = query.split()[1]
            speak(int(query.split()[0]) * int(query.split()[2]))

        elif there_exists(["לחלק ל","/"]):
            opr = query.split()[1]
            speak(int(query.split()[0]) / int(query.split()[2]))

        #MATH -END-

        elif 'תעשה ביטבוקס' in query:
            speak('boom ka boom boom boom ka boom boom ka boom boom boom ka boom boom ka boom boom boom ka boom boom ka boom boom boom ka boom')

        elif 'מה קורה' in query:
            speak("Everything's good, thanks for asking boss.")

        elif 'כבה מערכות' in query:
            speak("As your command.")
            quit()

        elif 'כיבוי מערכות' in query:
            speak("As your command.")
            quit()