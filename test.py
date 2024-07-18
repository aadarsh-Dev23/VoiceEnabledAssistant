import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Use the first available voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
