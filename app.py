import os
from random import randint

for i in range(1, 365):
    for j in range(0, 10):
     d = str(i) + 'days ago'
     with open('fle.txt', 'a') as File:
            File.write(d +  str(randint(0, 100)) )
    os.system('git add .')
    os.system('git commit -m "commit"')

os.system('git push -u origin main')
