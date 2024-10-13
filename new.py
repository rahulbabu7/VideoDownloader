import subprocess


# with gpu
url = input("Enter the URL: ")

# Adjust the ffmpeg command for GPU encoding (e.g., using NVIDIA's NVENC)
subprocess.run([
    'ffmpeg',
    '-i', url,
    '-c:v', 'h264_nvenc',  # Use NVENC for NVIDIA GPU
    '-b:v', '5M',          # Set video bitrate (adjust as needed)
    'op.mp4'
])