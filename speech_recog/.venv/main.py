import speech_recognition as sr

# Initialize the recognizer
sp = sr.Recognizer()

# Load the audio file (replace 'sample.wav' with your MP3 file)
audio_file = "audio(1).wav"

# Listen to the audio file and convert it to text
with sr.AudioFile(audio_file) as source:
    audio_data = sp.record(source)
    converted_text = sp.recognize_google(audio_data)

# Print the converted text
print(converted_text)
