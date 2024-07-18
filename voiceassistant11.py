import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    print("Assistant: " + text)
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, the speech recognition service is not available.")
            return ""

# Function to fetch weather information
def get_weather(city):
    api_key = '53e94aec70dfeeff8eb1c9155a9851d4'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    print(f"Requesting weather for {city} with URL: {complete_url}")
    response = requests.get(complete_url)
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Response JSON: {data}")
        main = data.get('main')
        if main:
            temperature = main.get('temp')
            feels_like = main.get('feels_like')
            temp_min = main.get('temp_min')
            temp_max = main.get('temp_max')
            pressure = main.get('pressure')
            humidity = main.get('humidity')
            weather_description = data['weather'][0].get('description')
            weather_report = (f"The temperature in {city} is {temperature} degrees Celsius with {weather_description}. "
                              f"It feels like {feels_like} degrees. The minimum temperature is {temp_min} degrees and the maximum temperature is {temp_max} degrees. "
                              f"The atmospheric pressure is {pressure} hPa and the humidity is {humidity}%.")
            return weather_report
        else:
            return f"Sorry, I couldn't fetch the weather information for {city}."
    else:
        error_message = response.json().get("message", "No error message provided")
        print(f"Error fetching weather data: {error_message}")
        return f"Sorry, I couldn't fetch the weather information for {city}. Error message: {error_message}"

# Function to get the current date and time
def get_date_time():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"The current date and time is {date_time_str}."

# Main function to start the voice assistant
def main():
    speak("How can I assist you today?")
    while True:
        command = listen()
        
        if "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                weather_report = get_weather(city)
                speak(weather_report)
        elif "date" in command or "time" in command:
            date_time = get_date_time()
            speak(date_time)
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
