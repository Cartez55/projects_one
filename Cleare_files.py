import shutil
import os
import glob

directory_patch = r'C:\Users\Professional\Desktop\Нерасортировано'
from_patch = r'C:\Users\Professional\Desktop'
extension = '*.mp3', '*.docx', '*.doc', '*.mp4', '*.pdf', '*.jpg', '*.png'

while True:
    for e in extension:
        for i in glob.glob(from_patch + '\\' + e):
            shutil.move(i, directory_patch)
