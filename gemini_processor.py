import google.generativeai as genai

def process_with_gemini(text, image_path, api_key):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.5-flash")  # valid multimodal model
    image = genai.upload_file(image_path)

    response = model.generate_content([text, image])

    combined_text = ""

    # Correct way to extract text from parts
    if hasattr(response, "candidates") and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, "content") and hasattr(candidate.content, "parts"):
                for part in candidate.content.parts:
                    if hasattr(part, "text"):
                        combined_text += part.text + " "

    if combined_text.strip() == "":
        combined_text = "[No text returned by Gemini]"

    return combined_text.strip()
