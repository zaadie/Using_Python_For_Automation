import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt',],
    "AUDIO" : ['.m4a', '.m4b', 'mp3'],
    "VIDEOS": ['.mov','avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffixes == value:
                return category


print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        filePath =Path(items
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        dirextoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            continue 
            directoryPath.mkdir()
        rilePath.rename(directoryPath.joinpath(filePath))

