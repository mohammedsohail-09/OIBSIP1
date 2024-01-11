import speech_recognition as sr
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import requests
import pyaudio
import datetime
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
# def get_time_and_date(timezone_name):
#     try:
#         # Get the time zone object
#         timezone = pytz.timezone(timezone_name)

#         # Get the current time in the specified time zone
#         current_time = datetime.datetime.now(timezone)

#         # Format the time and date
#         formatted_time = current_time.strftime("%H:%M:%S")
#         formatted_date = current_time.strftime("%Y-%m-%d")

#         return formatted_time, formatted_date

#     except:
#            raise pytz.UnknownTimeZoneError:
#     return:None, "Unknown time zone. Please provide a valid time zone."
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error making the request; {e}")
        return ""
    
#     # Speak a general introduction for the voice assistant
#     speak("I am a voice assistant. How may I help you")
#     user_timezone = input("Enter your desired time zone (e.g., 'America/New_York'): ")

# time, date = get_time_and_date(user_timezone)

def process_query(query):
    # if "time" in query:
    # speak("Current time in {user_timezone}: {time}")
    # speak("Current date in {user_timezone}: {date}")
    # elif
    # speak("date")
    if "hello" in query:
        speak("Hello! How can I help you today?")
    elif "how are you" in query:
        speak("I'm doing well, thank you!")
    elif "goodbye" in query:
        speak("Goodbye! Have a great day.")
    elif "open youtube"  in query.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open google" in query.lower():
        webbrowser.open("google.com")
    elif 'open code' in query.lower():
        webbrowser.open("C:\\Users\\MOHAMMED SOHAIL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
        exit()
    elif "open chrome" in query.lower():
        webbrowser.open("chrome.com")
    elif "open linkedin" in query.lower():
        webbrowser.open("linkedin.com")
    elif "open whatsapp" in query.lower():
        webbrowser.open("whatsapp.com")  
    elif "open music"  in query.lower():
        webbrowser.open("jiosaavn.com") 
    elif "open youtube"  in query.lower():
        webbrowser.open("https://www.youtube.com") 
    else:
        speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you today?")
    
    while True:
        query = listen()
        if query:
            process_query(query)
