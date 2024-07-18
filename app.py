import speech_recognition as sr
import google.generativeai as genai
import os
from test import text_to_speech
import re
from vision import capture_and_save_image


genai.configure(api_key="AIzaSyAHJzeWbF7nOc6_Op_r7ZL1DaEqIVAA4iY")

def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    while(True):

        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise. Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Please speak now.")

            # Capture the audio
            audio = recognizer.listen(source)

            try:
                # Recognize speech using Google Web Speech API
                print("Recognizing...")
                text = recognizer.recognize_google(audio)

                model = genai.GenerativeModel('gemini-1.5-flash')
                if "open chrome" in text.lower():
                    os.system("start chrome")
                    response_text = "Opening Google Chrome."
                elif "open youtube" in text.lower():
                    os.system("start chrome https://www.youtube.com")
                    response_text = "Opening YouTube in Google Chrome."
                elif "open spotify" in text.lower():
                    # Assuming Spotify is installed and accessible via system path
                    os.system("start spotify")
                    response_text = "Opening Spotify."

                elif "what do you see" in text.lower():
                    # Assuming Spotify is installed and accessible via system path
                    # Upload the file and print a confirmation.
                    capture_and_save_image()
                    sample_file = genai.upload_file(path="captured_image.jpg",
                                                    display_name="Captured image")

                    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
                    response = model.generate_content([sample_file, "Describe the picture"])
                    symbols_to_remove = ['#', '*']
                    clean_text = response.text

                    for symbol in symbols_to_remove:
                        clean_text = clean_text.replace(symbol, '')
                    text_to_speech(clean_text)

                else:
                    response = model.generate_content(text)
                    print(response.text)
                    symbols_to_remove = ['#', '*']
                    clean_text = response.text

                    for symbol in symbols_to_remove:
                        clean_text = clean_text.replace(symbol, '')
                    text_to_speech(clean_text)

            except sr.UnknownValueError:
                print("Google Web Speech API could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech API; {e}")
            except Exception as ex:
                print(f"Unexpected error: {ex}")
                text_to_speech("Sorry, something unexpected happened.")


if __name__ == "__main__":
    main()
