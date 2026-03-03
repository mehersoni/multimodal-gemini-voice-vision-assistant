# Multimodal AI Prototype

This project is a speech + image based AI assistant that:
1. Takes voice input  
2. Captures an image  
3. Sends both to Gemini API  
4. Receives AI response  
5. Speaks the reply using Text-to-Speech  

Project Structure:

Prototype/
│
├── main.py
├── speech_to_text.py
├── camera_capture.py
├── gemini_processor.py
├── text_to_speech.py
├── input.wav
├── captured_image.jpg
├── requirements.txt
└── README.md

File Descriptions:

main.py               → Main controller that runs the full pipeline  
speech_to_text.py     → Converts user voice (audio) into text using Vosk  
camera_capture.py     → Captures image from the webcam  
gemini_processor.py   → Sends text + image to Gemini API and gets AI response  
text_to_speech.py     → Converts Gemini reply into spoken audio  
input.wav             → Recorded user voice input  
captured_image.jpg    → Image captured from the camera  
requirements.txt      → List of required Python libraries  
README.md             → Project overview and instructions  

How to Run:

pip install -r requirements.txt  
python main.py
