import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

class VoiceAssistant:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()

        # Set voice to female if available
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)

        # Set speaking speed
        self.engine.setProperty('rate', 150)

        self.greet_user()

    def talk(self, text):
        print(f"YANA: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            self.talk("Good morning!")
        elif hour < 18:
            self.talk("Good afternoon!")
        else:
            self.talk("Good evening!")
        self.talk("I am your assistant Yana. How can I help you?")

    def take_command(self):
        command = ""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.listener.adjust_for_ambient_noise(source)
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'yana' in command:
                    command = command.replace('yana', '').strip()
                    print(f"You said: {command}")
                    return command
                else:
                    print("Wake word 'yana' not found.")
        except sr.UnknownValueError:
            self.talk("Sorry, I did not understand that.")
        except sr.RequestError:
            self.talk("Sorry, I'm having trouble connecting to the service.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.talk("Something went wrong. Please try again.")

        return ""

    def run(self):
        command = self.take_command()
        if not command:
            return

        if 'play' in command:
            song = command.replace('play', '').strip()
            if song:
                self.talk(f'Playing {song}')
                pywhatkit.playonyt(song)
            else:
                self.talk("Please tell me the name of the song.")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.talk('The current time is ' + time)

        elif 'who is' in command or 'what is' in command or 'tell me about' in command:
            person = command.replace('who is', '').replace('what is', '').replace('tell me about', '').strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                self.talk(info)
            except wikipedia.exceptions.DisambiguationError:
                self.talk("There are multiple results. Please be more specific.")
            except:
                self.talk("Sorry, I couldn't find information on that.")

        elif 'date' in command:
            self.talk('Sorry, I have a headache.')

        elif 'are you single' in command:
            self.talk('I am in a relationship with wifi.')

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            self.talk(joke)

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            self.talk('Goodbye! Talk to you later.')
            exit()

        else:
            self.talk("Sorry, I didn't get that. Please try again.")

# Main loop
assistant = VoiceAssistant()
while True:
    try:
        assistant.run()
    except KeyboardInterrupt:
        assistant.talk("Voice assistant stopped manually. Goodbye!")
        break
