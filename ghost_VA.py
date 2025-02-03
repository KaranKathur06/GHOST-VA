import pyttsx3
import speech_recognition as sr
import datetime
from tomlkit import document
import wikipedia
import webbrowser
import os
import arrow
import pywhatkit as kit
import subprocess as sp
from urllib.parse import quote
import pyautogui
import random
import pyjokes
import requests

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)
# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#this paths are according to my system you can change it to yours files/application's path iin your system just copy that path and paste according to your apps and enjoy it 
paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\kathu\\AppData\\Local\\Discord\\app-1.0.9028\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'valorant': "C:\\Riot Games\\VALORANT\\live\\VALORANT.exe",
    'VSCode': "C:\\Users\\kathu\\AppData\Local\\Programs\\Microsoft VS Code\\code.exe",
    'opera': "c:\\Users\\kathu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX Browser.exe",
    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'firefox': "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    'edge': "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    'notepadplusplus': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'vlc': "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    'spotify': "C:\\Users\\kathu\\AppData\\Roaming\\Spotify\\Spotify.exe", 
    'discord': "C:\\Users\\kathu\\AppData\\Local\\Discord\\app-1.0.9028\\Discord.exe",
    'skype': "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe",
    'zoom': "C:\\Users\\kathu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe", 
    'gitbash': "C:\\Program Files\\Git\\git-bash.exe",
    'cmd': "C:\\Windows\\System32\\cmd.exe",
    'anaconda': "C:\\ProgramData\\Anaconda3\\Scripts\\anaconda-navigator.exe",
    'jupyter': "C:\\ProgramData\\Anaconda3\\Scripts\\jupyter-notebook.exe",
    'taskmanager': "C:\\Windows\\System32\\Taskmgr.exe",
    'controlpanel': "C:\\Windows\\System32\\control.exe",
    'fileexplorer': "C:\\Windows\\explorer.exe",
    'photoshop': "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2018\\Photoshop.exe",  
    'illustrator': "C:\\Program Files\\Adobe\\Adobe Illustrator CC 2018\\Illustrator.exe", 
    'gimp': "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe",
    'outlook': "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
    'slack': "C:\\Users\\kathu\\AppData\\Local\\slack\\slack.exe", 
    'trello': "C:\\Program Files\\Trello\\Trello.exe",
    'steam': "C:\\Program Files (x86)\\Steam\\Steam.exe",
    'netflix': "C:\\Program Files\\Netflix\\Netflix.exe",
    'twitch': "C:\\Users\\kathu\\AppData\\Roaming\\Twitch\\Bin\\Twitch.exe",  
    'defender': "C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\4.18.2108.7-0\\MpCmdRun.exe", 
    'firewall': "C:\\Windows\\System32\\WF.msc",
    'virtualbox': "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe",
    'vmware': "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe",
    'onenote': "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE",
    'evernote': "C:\\Program Files (x86)\\Evernote\\Evernote\\Evernote.exe",
    'snippingtool': "C:\\Windows\\System32\\SnippingTool.exe",
    'taskscheduler': "C:\\Windows\\System32\\taskschd.msc",
    'charmap': "C:\\Windows\\System32\\charmap.exe",
}


def open_application(app_name):
    if app_name.lower() in paths:
        os.startfile(paths[app_name.lower()])
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, {name} {gender}. I don't have information on how to open {app_name}.")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def is_girl_name(name):
    # Simple heuristic: If the name ends with 'a', 'i', 'n', or 'l', consider it a girl's name
    return name.lower().endswith(('a', 'i',  'l'))


def greet_user():
    global gender, name
    current_hour = datetime.datetime.now().hour
    
    # Read user names from the file
    with open("user_names.txt", "r") as file:
        names = file.readlines()
    
    # Remove newline characters and strip leading/trailing spaces
    names = [name.strip() for name in names if name.strip()]
    
    # Take the last name as the most recent user
    if names:
        name = names[-1]
    else:
        name = "User"
    
    gender = "sir" if not is_girl_name(name) else "mam"

    if 6 <= current_hour < 12:
        speak(f"Good morning {name} {gender}!")
    elif 12 <= current_hour < 18:
        speak(f"Good afternoon {name} {gender}!")
    else:
        speak(f"Good evening {name} {gender}!")


def get_user_profile():
    while True:
        print("Hello! What's your name?")
        speak("Hello! What's your name?")
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            name = r.recognize_google(audio).lower()
            print(f"You: {name}\n")

            if name != 'none':
                with open("user_names.txt", "a") as file:
                    file.write(name + '\n')
                gender = "{gender}" if not is_girl_name(name) else "mem"
                return name

            else:
                print("Sorry, I didn't get that. Can you please repeat?")
                speak("Sorry, I didn't get that. Can you please repeat?")

        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Can you please repeat?")
            speak("Sorry, I didn't get that. Can you please repeat?")

        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            speak("Sorry, there was an issue with the speech recognition service.")


def listen():
    """Takes user input, recognizes it using Speech Recognition module, and converts it into text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # Adjust for ambient noise before listening
        r.adjust_for_ambient_noise(source)
        
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You: {query}\n")
        return query

    except sr.UnknownValueError:
        print(f"Sorry {gender}, I didn't get that. Can you please repeat?")
        return 'None'

    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return 'None'


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "your-api-id ", # Replace with your OpenWeatherMap API key 
        "units": 'imperial' and "metric" # Use "imperial" for Fahrenheit, "metric" for Celsius
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        main_weather = weather_data['main']
        temperature_f = main_weather['temp']
        temperature_c = (temperature_f - 32) * 5.0/9.0
        weather_description = weather_data['weather'][0]['description']

        result = f"The current weather in {city} is {temperature_f} degrees Fahrenheit or {temperature_c:.2f} degrees Celsius. {weather_description}."
        print(result)
        speak(result)
    else:
        print(f"Error: Unable to get weather information for {city}. Please check the city name and try again.")
        speak(f"Sorry, I couldn't retrieve weather information for {city}.")
   

def DayandTime():
    current_datetime = arrow.now()
    formatted_datetime = current_datetime.format("YYYY-MM-DD HH:mm:ss")
    speak(f"Your current date and time is {formatted_datetime}")
    print(f"Current date and time: {formatted_datetime}")

def search_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)
    speak(f"Searching YouTube for {query}. Enjoy your video!")

def play_on_youtube(query):
    if query:
        kit.playonyt(query)

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Searching Google for {query}. Here are the results.")


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
    send_button_x = 900  # Adjust the X-coordinate based on your system
    send_button_y = 700  # Adjust the Y-coordinate based on your system
    pyautogui.click(send_button_x, send_button_y)

def tell_joke():
    joke = pyjokes.get_joke()
    print("Joke: ", joke)
    speak(joke)


#------------------------------------------------------------MAIN FUNCTION---------------------------------------------------------------#

def main():
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    

    name = get_user_profile()
    greet_user()
    speak(f"I am your virtual assistant GHOST. How can I help you today {name} {gender}?")
    
    while True:
        query = listen()
        
        if query:
            query = query.lower() 

            if any(keyword in query for keyword in ['introduce yourself', 'who are you', 'tell me something about yourself', 'introduce yourself']): #you can also add your own words to access the function
                print('I am Ghost. You can call me as a personal computer and virtual assistant of Karan Kathur. I was created using Python. I am 1 day old. Currently, I am in the development stage.')
                speak('I am Ghost. You can call me as a personal computer and virtual assistant of Karan Kathur. I was created using Python. I am 1 day old. Currently, I am in the development stage.')
            
            elif any(keyword in query for keyword in ["shutdown system", "system off", "shutdown the system", "system shutdown"]): #you can also add your own words to access the function
                speak('Okay, the system will turn off in 30 seconds')
                os.system("shutdown /s /t 30")
            
            elif any(keyword in query for keyword in ["good", "thank you", "thanks", "well done"]): #you can also add your own words to access the function
                greetings = ["Good!", "Thank you!", "Thanks!", "Well done!"]
                greet = random.choice(greetings)
                speak(greet)

            elif any(keyword in query for keyword in ["how's everything", "how are you", "how you doing", "how are you doing", "what's up", "whatsup"]):
                greetings = ["I am well, thanks for asking.", "I am well.", "Doing great."]
                greet = random.choice(greetings)
                speak(greet)


            elif 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)

            elif 'just only open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            
            elif 'youtube' in query:
                speak('What do you want to search on YouTube, {gender}?')
                query = listen().lower()
                query = query.replace("youtube", "") 
                search_youtube(query)

            elif 'play video' in query:
                speak('What do you want to play on Youtube, {gender}?')
                query = listen().lower()
                play_on_youtube(query)

            elif 'Google' in query:
                speak('What do you want to search on Google, {gender}?')
                query = listen().lower()
                query = query.replace("search on Google", "")
                search_google(query)
                        

            elif 'play music' in query:
                os.startfile(paths['spotify'])
                speak("Opening Spotify. Enjoy your music!")
            
            elif "send whatsapp message" in query:
                speak('On what number should I send the message {gender}? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message {gender}?")
                message = listen().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message {gender}.")

            elif "date and time" in query:
                DayandTime()
                continue

            elif name.lower() in query:
                greet_user()

            elif 'open' in query and any(app in query for app in paths.keys()):
                app_name = next((app for app in paths.keys() if app in query), None)
                open_application(app_name)

            elif any(keyword in query for keyword in['tell me some jokes', 'make me laugh' , 'crack joke', 'make atmosphere funny']): #you can also add your own words to access the function
                tell_joke()

            elif any(keyword in query for keyword in['tell me current wheather','cheak wheather update','cheak current wheather']): #you can also add your own words to access the function
                speak("tell me your city")
                print("tell me your city")
                city = listen()
                get_weather( city)

            elif 'exit' in query:
                speak(f"Goodbye {name} {gender}!")
                break

if __name__ == "__main__":
    main()
