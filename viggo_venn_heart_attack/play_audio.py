from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("oneMoreTime.wav")
play(song)