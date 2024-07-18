Voice-Activated AI Assistant
This repository contains a voice-activated AI assistant that integrates speech recognition, generative AI, and image capture. The assistant listens for specific voice commands to perform tasks like opening applications, capturing and describing images, and responding to general queries.

Features
Speech Recognition: Utilizes the speech_recognition library to capture and process audio input from the microphone.
Generative AI: Uses Google's generative AI to generate responses and describe images.
Voice Commands: Recognizes specific phrases to execute predefined tasks:
Open Google Chrome
Open YouTube
Open Spotify
Capture and describe images
Text-to-Speech: Converts generated text responses to speech for auditory feedback.
Image Capture and Analysis: Captures images using a webcam, uploads them for analysis, and generates a description of the captured images.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/voice-activated-ai-assistant.git
cd voice-activated-ai-assistant
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your Google Generative AI API key:

python
Copy code
genai.configure(api_key="YOUR_API_KEY")
Usage
Run the main script to start the voice-activated assistant:

bash
Copy code
python main.py
Speak the following commands to interact with the assistant:

"Open Chrome"
"Open YouTube"
"Open Spotify"
"What do you see" (to capture and describe an image)
File Structure
main.py: Main script to run the voice-activated assistant.
requirements.txt: List of required Python packages.
vision.py: Module for capturing and saving images.
test.py: Module for text-to-speech functionality.
