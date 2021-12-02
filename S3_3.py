import subprocess

subprocess.call(["ffmpeg", "-i", "cut_video.mp4",
                 "-f", "mpegts", "udp://127.0.0.1:23000"])