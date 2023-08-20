# Audiobook-maker-using-TTS
Creating Audiobooks from PDF files using open-source TTS 

this is an audiobook generator that uses the pre-trained models of Coqui ai's text-to-speech model https://github.com/coqui-ai/TTS to generate audiobooks from PDFs, 
I tested all the models and number 23 was the most successful, 
The code is written in Jupyter format for ease of use. Ensure the code file and the pdf are in the same directory alone. The generation process is lengthy,
at least on my low-power CPU, it took 4 hours for a 200-page book to be made, it will be faster on yours for sure.
I used Ubunutu 20.04, not sure if it works on other systems (check TTS git page) 
after generation, there will be many files in the folder but you only need "merged_audio.wav", all the others are individual pages, unless specifically needed feel free to delete
use PIP to install all dependencies, 
Good Luck 
