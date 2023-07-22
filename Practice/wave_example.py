# Audio file formats
# .mp3 is lossy compression
# .flac is lossless compression
# .wav is compressionless

import wave

# Audio signal parameters
# -- number of channels
# -- sample width
# -- framerate/sample_rate
# -- number of frames
# -- values of a frame

obj = wave.open("01-basics_output.wav", "rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)
obj.close()

obj_new = wave.open("01-basics_output-new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(1)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)
obj_new.close()
