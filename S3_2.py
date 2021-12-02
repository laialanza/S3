import subprocess

subprocess.call(["ffmpeg", "-i", "output_vp8.webm", "-i", "output_vp9.webm",
                 "-filter_complex", "[0][1]vstack", "joinedvideo.mp4"])