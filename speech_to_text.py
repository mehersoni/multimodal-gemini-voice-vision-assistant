import json
from vosk import Model, KaldiRecognizer

def convert_speech_to_text(audio_file="input.wav"):
    # Load Vosk model
    model = Model("vosk-model-small-en-us-0.15")
    rec = KaldiRecognizer(model, 16000)

    with open(audio_file, "rb") as f:
        while True:
            data = f.read(4000)  # read in small chunks
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

    # Get the final result
    result = rec.FinalResult()
    text = json.loads(result).get("text", "")

    return text

