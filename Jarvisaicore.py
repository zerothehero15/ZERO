import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Initialize the recognizer and the speaker
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice and recognize it
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, I am having trouble connecting to the speech service.")
        return None

# Main function that processes commands
def jarvis():
    speak("Hello, I am Jarvis. How can I assist you today?")

    while True:
        command = listen()

        if command:
            # Basic commands
            if 'wikipedia' in command:
                speak("Searching Wikipedia...")
                query = command.replace("wikipedia", "").strip()
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    speak(f"According to Wikipedia, {summary}")
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple entries for this. Can you be more specific?")
                except wikipedia.exceptions.PageError:
                    speak("I could not find anything on Wikipedia for that.")

            elif 'open google' in command:
                speak("Opening Google.")
                webbrowser.open("https://www.google.com")

            elif 'open youtube' in command:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")

            elif 'what is your name' in command:
                speak("I am Jarvis, your voice assistant.")

            elif 'stop' in command or 'exit' in command:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I didn't understand that.")

# Start the assistant
if __name__ == "__main__":
    jarvis()

