import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6318830e6688432ba350f5677a61477e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
   
   import google.generativeai as genai

def aiProcess(command):
    # Initialize the API client (if needed)
    # For example, if there’s an API key setup method
    genai.configure(api_key="AIzaSyCtGPb45Td-dEiTuMT2InJFp7sIoPLaTcI")

    # Create a model instance (adjust based on actual API)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Start a chat session or send a message (update based on actual API)
    chat = model.start_chat()
    response = chat.send_message(command)
    
    return response.text


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedIn" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open amazon" in c.lower():
        webbrowser.open("http://www.amazon.in")
    elif "open flipkart" in c.lower():
        webbrowser.open("http://www.flipkart.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if the request was successful
        if r.status_code == 200:
        # Parse the JSON data
             data = r.json()

        # Extract the articles into a list
        articles = data.get('articles',[])

        # Print the articles
        for article in articles:
            speak(article['title'])

    else:
        # Let the gen-ai handle the request
        output = aiProcess(c)
        speak(output)





if __name__== "__main__":
    speak("Initializing Jarvis....")
    while True:
      # Listen for the wake word "Jarvis"
      # obtain audio from the microphone
      r = sr.Recognizer()
     

      print("Recognizing...")
      try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        word = recognizer.recognize_google(audio) # to recognize google
        if word.lower()=="jarvis":
            speak("Ya")
            # Listen For Command

            with sr.Microphone() as source:
             print("Jarvis Active,  listening for command...")
             audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
             command =  recognizer.recognize_google(audio)

             processCommand(command)



      except sr.UnknownValueError:
         print("Could Not understand audio.")
      except sr.RequestError as e:
          print("Could not request results; {0}".format(e))
      except Exception as e:
            print("Error; {0}".format(e))