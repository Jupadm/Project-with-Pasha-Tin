from pydub import AudioSegment

f = open("Bird_list.txt", "r")
for line in f:
    line = line.rstrip()
    name_mp3 = line + ".mp3"
    name_ogg = line + ".ogg"

    AudioSegment.from_mp3(name_mp3).export(name_ogg, format='ogg')

f.close()
