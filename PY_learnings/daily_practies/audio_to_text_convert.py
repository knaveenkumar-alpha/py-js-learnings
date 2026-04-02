import speech_recognition as sr
from pydub import AudioSegment

def audio_to_text(audio_file_path):
    """
    Convert an audio file to text using SpeechRecognition.

    Parameters:
        audio_file_path (str): Path to the audio file.

    Returns:
        str: Transcribed text from the audio.
    """
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Convert audio to WAV format if necessary
    audio_file = audio_file_path
    if not audio_file_path.endswith(".wav"):
        audio = AudioSegment.from_file(audio_file_path)
        audio_file = audio_file_path.replace(audio_file_path.split(".")[-1], "wav")
        audio.export(audio_file, format="wav")

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        print("Processing audio...")
        audio_data = recognizer.record(source)

    # Recognize (convert to text)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription successful.")
        return text
    except sr.UnknownValueError:
        return "Unable to understand audio."
    except sr.RequestError as e:
        return f"Error with the recognition service: {e}"

# Example usage
if __name__ == "__main__":
    input_audio = "path/to/your/audiofile.mp3"  # Replace with your file path
    transcription = audio_to_text(input_audio)
    print("Transcribed Text:", transcription)
