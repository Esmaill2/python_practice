# import os
# from glob import glob

# pattern = {
#     'photos':['*.jpg','*.png']
#     ,'videos':['*.mp4','*.mkv']
#     ,'text':['*.txt']
#     ,'CR2':['*.CR2']
# }
# for x in pattern :
#  os.makedirs(str(x), exist_ok=True)

# for y,z in pattern.items():
#   print(y)
#   files = [ ]
#   for x in z:
#    files += glob(x)
#   for a in files:
#    os.replace(a , f'{y}/{a}')


import os
from glob import glob


pattern = {"photos":["*.jpg","*.jpeg","*.png","*.gif","*.bmp","*.tiff","*.webp","*.svg","*.ico","*.heic","*.raw","*.psd","*.ai"],
           "videos":["*.mp4","*.mkv","*.avi","*.mov","*.flv","*.wmv","*.webm","*.m4v","*.mpg","*.mpeg","*.3gp","*.ogv","*.ts","*.mts","*.m2ts"],
           "text":["*.txt","*.doc","*.docx","*.pdf","*.xls","*.xlsx","*.csv","*.md","*.rtf","*.odt"],
           "CR2":["*.CR2","*.cr2"]}
for x in pattern:
    os.makedirs(str(x), exist_ok=True)

for folder, extensions in pattern.items():
    for dot in extensions:
        files = glob(dot)
        for file in files:
            if file == "log.txt":
                continue
            os.replace(file, f"{folder}/{file}")
            # print (f'{file.upper()} moved to {folder.upper()}')
            with open("log.txt", "a") as log:
                log.write(f"{file} moved to {folder}\n")
