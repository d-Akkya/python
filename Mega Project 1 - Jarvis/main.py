import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from newsapi import newsapi
import requests
# from openai import OpenAI
# from client import client
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running so music can play fully
    while pygame.mixer.music.get_busy():  # Check if music is playing
        pygame.time.Clock().tick(10)  # Prevents high CPU usage in loop

    # Unload the MP3 file
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# def aiProcess(command):
#     client = client.api_key()

#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

#     return completion.choices[0].message


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/in/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # Make the request to the News API
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if the request was successful
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
    
            # Extract the articles
            articles = data.get('articles', [])

            # Speak the headlines
            for article in data["articles"]:
                speak(article["title"])
        else:
            print("Failed to retrieve data:", response.status_code)

    else:
    #     # Let OpenAI handle the request
    #     output = aiProcess(c)
    #     speak(output)
        speak('Try our premium with chat-gpt')


if __name__ == "__main__":
    speak('Initializing Jarvis....')
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except Exception as e:
            print("Error; {0}".format(e))