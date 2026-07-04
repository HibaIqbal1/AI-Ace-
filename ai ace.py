import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import pywhatkit
from openai import OpenAI

# ======================
# OPENROUTER API KEY
# ======================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="PASTE_YOUR_NEW_OPENROUTER_API_KEY_HERE"
)

# ======================
# VOICE ENGINE
# ======================

engine = pyttsx3.init()

def speak(text):
    print("Hiba's AI Ace:", text)

    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

# ======================
# LISTEN
# ======================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:

        return ""

# ======================
# AI RESPONSE
# ======================

def ask_ai(question):

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role":"system",
                "content":"You are Hiba's AI Ace."
            },
            {
                "role":"user",
                "content":question
            }
        ]
    )

    return response.choices[0].message.content

# ======================
# MAIN LOOP
# ======================

speak("Hello Hiba. I am your AI Ace.")

while True:

    command = listen()

    if not command:
        continue

    if "exit" in command:
        speak("Goodbye")
        break

    elif "open google" in command:

        webbrowser.open("https://google.com")

        speak("Opening Google")

    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        speak("Opening YouTube")

    elif "open linkedin" in command:

        webbrowser.open("https://linkedin.com")

        speak("Opening LinkedIn")

    elif "open whatsapp" in command:

        webbrowser.open(
            "https://web.whatsapp.com"
        )

        speak("Opening WhatsApp")

    elif "open calculator" in command:

        subprocess.Popen("calc.exe")

        speak("Opening Calculator")

    elif "open notepad" in command:

        subprocess.Popen("notepad.exe")

        speak("Opening Notepad")

    elif command.startswith("play "):

        song = command.replace(
            "play ",
            ""
        )

        pywhatkit.playonyt(song)

        speak(f"Playing {song}")

    else:

        answer = ask_ai(command)

        speak(answer)