import os 
from glob import glob
folders = ['photos','videos','text','CR2']
for x in folders:
 os.makedirs(x, exist_ok=True)

photos = glob('*.jpg') + glob('*.png') + glob('*.psd') + glob('*.svg')
videos = glob('*.gif') + glob('*.mkv') + glob('*.mp4')
text = glob('*.txt')
CR2 = glob('*.CR2')

for e        in photos:
  os.replace(f'{e}',f'photos/{e}')

for e in text:
  os.replace(f'{e}',f'text/{e}')

for e in videos:
  os.replace(f'{e}',f'videos/{e}')

for e in CR2:
  os.replace(f'{e}',f'CR2/{e}')