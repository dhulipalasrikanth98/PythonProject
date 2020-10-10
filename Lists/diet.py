from pygame import mixer
from time import time
from datetime import datetime
def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        k=input()
        if k==stopper:
            logfile(k)
            mixer.music.stop()
            break
def logfile(k):
    if k=='done':
        with open('newfile.txt','a') as f:
            f.write(f"water drinked ?{k} at {datetime.now()}\n")
    elif k=='eyedone':
         with open('newfile.txt','a') as f:
            f.write(f"excercise for  ?{k} at {datetime.now()}\n")
    if k=='phydone':
         with open('newfile.txt','a') as f:
            f.write(f"physical excercise ?{k} at {datetime.now()}\n")


    mixer.music.stop()
if __name__=='__main__':
    init_water=time()
    init_eye=time()
    init_phy = time()
    s=5
    k=7
    l=8
    while True:
        if time()-init_water>s:
            print("enter done to stop")
            musicloop('drinking-water.ogg','done')
            
            init_water=time()
        if time() - init_eye>k:
            print("enter eyedone if eye excesrcise done")
            musicloop('drinking-water.ogg','eyedone')
            init_eye=time()
        if time()-init_phy>l:
            print("enter phydone if physical excercise is done")
            musicloop('drinking-water.ogg','phydone')
            init_phy=time()


        
