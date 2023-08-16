# Imports
import os
import PyPDF2
from TTS.api import TTS
from pydub import AudioSegment

# Initialize file and path
pdf_filename = 'name'
pdf_path = os.path.expanduser(f'~/audiobooks/{pdf_filename}')
input_dir = os.path.expanduser('~/audiobooks/')
output_dir = os.path.expanduser('~/audiobooks/')

# Initialize TTS engine
model_name = TTS.list_models()[17]
tts = TTS(model_name)

# List to store audio and text segments
audio_segments = []
cleaned_text_segments = []
merged_text = ""

# Open and read the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    # Loop through pages and convert text to speech
    for num in range(num_pages):
        try:
            page = pdf_reader.pages[num]
            text1 = page.extract_text()

            if not text1.strip():
                continue

            # Remove commas and periods from the extracted text
            cleaned_text = text1.replace(',', '').replace('.', '')

            # Append the cleaned text to the list of segments
            cleaned_text_segments.append(cleaned_text)

            # Join the cleaned text segments into a single string
            merged_text = ' '.join(cleaned_text_segments)

            audio_filename = f'page_{num + 1}.wav'
            audio_path = os.path.join(output_dir, audio_filename)
            tts.tts_to_file(text=merged_text, speaker=tts.speakers[0], file_path=audio_path, speed=1.5, emotion="Happy")

            # Load the audio segment and append to the list
            audio_segment = AudioSegment.from_wav(audio_path)
            audio_segments.append(audio_segment)

            # Clear the lists for the next iteration
            cleaned_text_segments.clear()
            audio_segments.clear()

        except Exception as e:
            print(f"An exception occurred: {e}")
            print("Restarting loop from the last index where the error occurred.")
            continue  # Restart the loop from the last index where the error occurred

# Get a list of all WAV files in the input directory
wav_files = [f for f in os.listdir(input_dir) if f.startswith('page_') and f.endswith('.wav')]

# Sort the WAV files based on the page numbers in their filenames
sorted_wav_files = sorted(wav_files, key=lambda f: int(f.split('_')[1].split('.')[0]))

# Load and append audio segments in the sorted order
for wav_file in sorted_wav_files:
    wav_path = os.path.join(input_dir, wav_file)
    audio_segment = AudioSegment.from_wav(wav_path)
    audio_segments.append(audio_segment)

# Concatenate audio segments into a single audio file
merged_audio = AudioSegment.empty()
for segment in audio_segments:
    merged_audio += segment

# Save the merged audio to a file
merged_audio_filename = 'merged_audio.wav'
merged_audio_path = os.path.join(output_dir, merged_audio_filename)
merged_audio.export(merged_audio_path, format='wav')

print(f"Merged audio saved to '{merged_audio_path}'.")
