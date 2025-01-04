# GHOST - Your Virtual Assistant

GHOST is a personal virtual assistant built using Python. It provides a range of functionalities such as voice recognition, text-to-speech, web browsing, and application management. GHOST can perform tasks like searching Wikipedia, playing music, sending WhatsApp messages, checking the weather, and more.

---

## Features

- **Voice Recognition**: Understands user commands through speech.
- **Text-to-Speech**: Responds to user queries with voice output.
- **Application Management**: Opens various applications installed on your system.
- **Web Browsing**: Searches Google and YouTube based on user queries.
- **Weather Updates**: Provides current weather information for specified cities.
- **Jokes**: Tells jokes to lighten the mood.
- **WhatsApp Messaging**: Sends messages via WhatsApp Desktop or WhatsApp Web.
- **Date and Time**: Provides the current date and time.

---

## Requirements

### Python Version
- Python 3.x

### Libraries
The following libraries are required:

- `pyttsx3`
- `speech_recognition`
- `datetime`
- `wikipedia`
- `webbrowser`
- `os`
- `arrow`
- `pywhatkit`
- `pyautogui`
- `requests`
- `pyjokes`
- `configparser`
- `logging`

Install the required libraries using pip:

```bash
pip install pyttsx3 speech_recognition wikipedia pywhatkit pyautogui requests pyjokes arrow
```

---

## Setup

1. Clone or download the repository to your local machine.
2. Ensure that all required libraries are installed.
3. Update the `paths` dictionary in the code to match the installation paths of applications on your system.
4. Replace the OpenWeatherMap API key in the `get_weather` function with your own API key.
5. Create a text file named `user_names.txt` in the same directory to store user names.

---

## Usage

Run the script using Python:

```bash
python your_script_name.py
```

Follow the voice prompts to interact with GHOST. Use voice commands to perform various tasks.

### Example Commands

- "Open Notepad"
- "Search Wikipedia for Python programming"
- "Play music"
- "Tell me a joke"
- "What's the weather in [city]?"
- "Send WhatsApp message to [number]"

---

## Logging

GHOST logs errors and important events to a file named `assistant.log` for debugging purposes.

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Contributions are welcome and appreciated!

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- Thanks to the developers of the libraries used in this project.
- Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing weather data.
