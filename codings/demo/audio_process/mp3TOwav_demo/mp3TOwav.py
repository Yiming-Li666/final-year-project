from os import path
from pydub import AudioSegment
 
# files                                                                         
src = "this.mp3"
dst = "that.wav"
 
# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")