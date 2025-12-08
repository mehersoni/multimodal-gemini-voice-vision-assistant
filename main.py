from audio_input import record_audio
from speech_to_text import convert_speech_to_text
from camera_capture import capture_image
from gemini_processor import process_with_gemini
from text_to_speech import speak_text
from config import GEMINI_API_KEY, AUDIO_FILE, IMAGE_FILE

# 1. Record Voice
record_audio(AUDIO_FILE)

# 2. Speech → Text
user_text = convert_speech_to_text(AUDIO_FILE)

# 3. Capture Image
capture_image(IMAGE_FILE)

# 4. Gemini Processing
gemini_reply = process_with_gemini(user_text, IMAGE_FILE, GEMINI_API_KEY)
print("Gemini Reply:", gemini_reply)

# 5. Speak Output
speak_text(gemini_reply)
