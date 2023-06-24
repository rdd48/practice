import sys
import subprocess

try:
    file = sys.argv[1]
except:
    exit('Provide file! USAGE: python yt-dlp.py FILENAME')

with open(file) as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    for l in lines:
        if not l.startswith('#'):
            subprocess.run(f"yt-dlp -x --audio-format mp3 '{l}'", shell=True)

