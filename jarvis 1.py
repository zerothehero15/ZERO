import requests
import webbrowser
from math import *
from pytube import Search


# Jarvis Assistant App
def jarvis():
    print("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = input("Enter your command: ").lower()

        if 'weather' in command:
            get_weather()
        elif 'calculate' in command:
            calculate()
        elif 'search internet' in command:
            search_internet(command)
        elif 'search youtube' in command:
            search_youtube(command)
        elif 'exit' in command:
            print("Goodbye!")
            break
        else:
            print("I didn't understand that. Please try again.")


# Function to get weather
def get_weather():
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        weather_desc = data['weather'][0]['description']
        print(f"Weather in {city}: {weather_desc.capitalize()}, Temperature: {temperature}°C")
    else:
        print("City not found, please try again.")


# Function to handle calculations
def calculate():
    expression = input("Enter the mathematical expression (e.g., 2 + 2): ")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except:
        print("Invalid mathematical expression.")


# Function to search the internet
def search_internet(command):
    query = input("Enter your search query: ")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    print(f"Searching Google for: {query}")


# Function to search YouTube
def search_youtube(command):
    query = input("Enter YouTube search query: ")
    search = Search(query)
    videos = search.results[:5]  # Get the first 5 results
    for i, video in enumerate(videos):
        print(f"{i + 1}. {video.title} ({video.watch_url})")


# Start Jarvis
if __name__ == "__main__":
    jarvis()
