# 🎙️ Your Alexa-like AI Named Assistant in Python – YANA

A smart and interactive voice assistant built using Python. This assistant listens to your commands and performs actions like playing music, telling the time, searching Wikipedia, and even cracking jokes! It’s designed to be lightweight and friendly — like your own desktop Alexa or Siri! 🧠✨

---

## 🚀 Features

| Feature             | Library Used         | Trigger Word(s)             | Example Command                     | Assistant Response                            |
|---------------------|----------------------|------------------------------|-------------------------------------|-----------------------------------------------|
| 🎧 Voice Recognition | `speech_recognition` | "yana" (wake word)           | `yana play despacito`              | "Playing despacito"                           |
| 🔊 Text-to-Speech    | `pyttsx3`            | —                            | `—`                                | "I am in a relationship with wifi"            |
| 🎵 Play YouTube Song | `pywhatkit`          | `play`                       | `yana play shape of you`           | "Playing shape of you"                        |
| 🕒 Tell Time         | `datetime`           | `time`                       | `yana what time is it`             | "The current time is 03:45 PM"                |
| 📚 Wikipedia Search  | `wikipedia`          | `who is`, `what is`          | `yana who is Elon Musk`            | "Elon Musk is a business magnate and investor." |
| 😂 Tell Jokes        | `pyjokes`            | `joke`                       | `yana tell me a joke`              | "Why do programmers prefer dark mode?..."     |
| ❌ Exit App          | —                    | `stop`, `exit`, `bye`        | `yana stop`                         | "Goodbye! Talk to you later."                 |
| 🙋‍♂️ Greeting         | `datetime` + TTS     | —                            | (on start)                         | "Good morning! I am your assistant Yana..."   |

---


---

## ⚙️ How It Works

1. **Wake Word Activation**: The assistant activates when it hears the wake word `"yana"`.
2. **Voice Capture**: Uses your microphone to capture speech input.
3. **Command Processing**: Interprets commands like:
   - 🔊 "Play [song name]" on YouTube
   - 📚 "Who is..." / "What is..." queries via Wikipedia
   - 🕒 Tells time
   - 😂 Tells jokes
4. **Voice Response**: Speaks back using `pyttsx3`.

---

## 🛠️ Requirements

- Python 3.6 or higher
- Internet connection (for speech recognition & online features)
- Working Microphone


### 🧠 Technologies Used

- **SpeechRecognition** – Convert voice to text
- **pyttsx3** – Text-to-speech conversion (offline)
- **pywhatkit** – Play YouTube songs using voice
- **wikipedia** – Fetch short summaries
- **pyjokes** – Get random programming jokes
- **datetime** – Time-based greetings and clock

---

## 🙋‍♀️ Author

**Shriyani Teli**

- 🔗 [GitHub Profile](https://github.com/shriyani18)  
- 📫 *Feel free to connect and contribute!*

---

🧠 **Tip**  
Use headphones and a quiet environment for better voice recognition accuracy.

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt

---
