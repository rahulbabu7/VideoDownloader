# import requests
import subprocess

url = input("Enter the url")

# r = requests.get(url)

# print(r.text)
subprocess.run(['ffmpeg', '-i', url,"output.mp4"]);