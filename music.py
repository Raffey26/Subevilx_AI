import os
import random

n=random.randint(0,119)
print(n)

music_dir='C:\\Users\\dawood\Music\\songs\\NCS'
songs=os.listdir(music_dir)
print(songs)
os.startfile(os.path.join(music_dir,songs[n])) 