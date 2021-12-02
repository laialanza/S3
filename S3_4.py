import subprocess

host = input("Choose an IP address? \n")
host_port = ("udp://"+ host + ":23000")
subprocess.call(["ffmpeg", "-i", "cut_video.mp4",
                 "-f", "mpegts", host_port])