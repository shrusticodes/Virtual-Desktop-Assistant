import speech_recognition as sr    
import pyttsx3                     
import datetime  
import time                                   
import webbrowser                                                               
import subprocess                  
from tkinter import *              
import pyjokes                     
name_assistant = "Sahaya"
engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait() 
def wishMe():
  hour=datetime.datetime.now().hour
  if hour >= 0 and hour < 12:
      speak("Hello,Good Morning")
  elif hour >= 12 and hour < 18:
      speak("Hello,Good Afternoon")
  else:
      speak("Hello,Good Evening")
def get_audio(): 
    r = sr.Recognizer() 
    audio = '' 
    with sr.Microphone() as source: 
        print("Listening") 
        audio = r.listen(source, phrase_time_limit = 3) 
        print("Stop.")  
    try: 
        text = r.recognize_google(audio, language ='en-in') 
        print('You: ' + ': ' + text)
        return text
    except:
        return "None"
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')
wishMe()
def Process_audio():
    run = 1
    if __name__=='__main__':
        while run==1:
            statement = get_audio().lower()
            results = ''
            run +=1
            if "hello" in statement or "hi" in statement:
              wishMe()               
            if "ok bye" in statement:
                speak('Your personal assistant ' + name_assistant +' is shutting down, Good bye')
                screen.destroy()
                break
            if 'joke' in statement:
              speak(pyjokes.get_joke())    
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)
            if 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)
            if 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Google Mail open now")
                    time.sleep(5)
            if 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Netflix open now")
            if 'open prime video' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")
                    time.sleep(5)     
            if 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)
            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)
            if 'corona' in statement or 'covid' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)
            if 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            if 'date' in statement:
                date()
            if 'who are you' in statement or 'what can you do' in statement or 'what is your name' in statement:
                    speak('I am Sahaya your personal assistant . I am programmed to minor tasks like opening youtube, taking notes, gmail etc') 
            if 'make a note' in statement:
                statement = statement.replace("make a note","")
                note(statement)        
            speak(results)
def main_screen():
      global screen
      screen = Tk()
      screen.title("Your Personal Virtual Assistant")
      screen.geometry("500x580")
      name_label = Label(text = "Sahaya",width = 300, bg = "black", fg="silver", font = ("Calibri", 27))
      name_label.pack()
      microphone_photo = PhotoImage(file = r"C:\Users\assistant.png")
      microphone_button = Button(image=microphone_photo, command = Process_audio)
      microphone_button.pack(pady=5)
      screen.mainloop()
main_screen()