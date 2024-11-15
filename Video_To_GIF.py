from moviepy.editor import *
video = VideoFileClip("C:\Python_AK\Ak.mp4").subclip(00,5)
video.write_gif("Akash.gif")