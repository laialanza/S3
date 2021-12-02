import subprocess

video = input("Introduce video's directory: \n")

answer=True
while answer!="5":
    print("""
        1. Convert to VP8
        2. Convert to VP9
        3. Convert to to h265
        4. Convert to AV1
        5 Exit
    """)
    answer = input("What would you like to do? \n")
    print("""
        Which video size you want
            1. 720p
            2. 480p
            3. 360x240
            4. 160x120
        """)
    video_chosen = input("What would you like to do? \n")
    if video_chosen == "1":
        video = "resized_video_720p.mp4"
    elif video_chosen == "2":
        video = "resized_video_480p.mp4"
    elif video_chosen == "3":
        video = "resized_video_360x240.mp4"
    elif video_chosen == "4":
        video = "resized_video_160x120.mp4"

    if answer == "1":
        subprocess.call(["ffmpeg","-i", video, "-c:v", "libvpx", "-b:v", "1M",
                         "-c:a", "libvorbis", "output_vp8.webm"])
    elif answer == "2":
        subprocess.call(["ffmpeg", "-i", video, "-c:v", "libvpx-vp9", "-b:v", "1M",
                         "-c:a", "libvorbis", "output_vp9.webm"])
    elif answer == "3":
        subprocess.call(["ffmpeg","-i", video, "-c:v", "libx265", "-crf", "26",
                         "-preset", "fast", "output_h265.mp4"])
       # subprocess.call(["ffmpeg", "-i", video,"-c:v", "libx265", "-vtag", "hvc1",
                       #  "-c:a", "copy","output_h265.mp4"])
    elif answer =="4":
        subprocess.call(["ffmpeg", "-i", video, "-c:v", "libaom-av1", "-crf", "30",
                         "-b:v", "0", "output_av1.mp4"])
    # To exit
    elif answer == 5:
        answer = False
        break;
    # Wrong command
    else:
        print("Write a valid command")