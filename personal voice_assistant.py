import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)

            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("Listening timeout. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")
            return ""

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

        except Exception as e:
            speak("An unexpected error occurred.")
            print(e)
            return ""

def open_application(app_name):

    applications = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe"
    }

    if app_name in applications:
        os.system(applications[app_name])
        speak(f"Opening {app_name}")

    else:
        speak("Application not found.")

def search_web(query):

    if query.strip() == "":
        speak("Please say something to search.")
        return

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

    speak(f"Searching for {query}")

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current_time}")

def search_wikipedia(topic):

    try:
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")

    except wikipedia.exceptions.PageError:
        speak("No information found.")

    except Exception:
        speak("Wikipedia service error.")

def process_command(command):

    if "open notepad" in command:
        open_application("notepad")

    elif "open calculator" in command:
        open_application("calculator")

    elif "open paint" in command:
        open_application("paint")

    elif "time" in command:
        tell_time()

    elif "search" in command:
        query = command.replace("search", "")
        search_web(query)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        search_wikipedia(topic)

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Command not recognized.")

def show_commands():

    print("\n========== SAMPLE COMMANDS ==========")
    print("1. Open Notepad")
    print("2. Open Calculator")
    print("3. Open Paint")
    print("4. Search Python Programming")
    print("5. What is the time")
    print("6. Wikipedia Artificial Intelligence")
    print("7. Exit")
    print("=====================================\n")

def main():

    speak("Personal Voice Assistant Started")

    show_commands()

    while True:

        command = listen()

        if command != "":
            process_command(command)

if __name__ == "__main__":
    main()
