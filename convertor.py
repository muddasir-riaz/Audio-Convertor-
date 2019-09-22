import os
import tempfile
from pydub import AudioSegment 

#iterating through the directory 
directory = 'ADD PATH'
counter = 0
#loop to convert mp3 to .wav
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        src = filename
        dst = "test"+filename+str(counter)
        counter += 1

        #convert mp3 to wav
        sound = AudioSegment.from_file('ADD PATH'+filename)
        
    continue
