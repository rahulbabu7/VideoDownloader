import subprocess

# Get the URL from the user
url = input("Enter the URL: ")

ffmpeg_command = ['yt-dlp', '-f', 'bestvideo+bestaudio', '--merge-output-format','mp4',url]
subprocess.run(ffmpeg_command)

