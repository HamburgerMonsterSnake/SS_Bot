import pyautogui as pg
import random
import time
try:
    while(1):
        pg.click()
        tmp = random.randint(1,5)
        if tmp == 1:
            pg.press('w')
        elif tmp == 2:
            pg.press('a')
        elif tmp == 3:
            pg.press('s')
        elif tmp == 4:
            pg.press('d')
        else:
            pg.press('space')
        time.sleep(100)
except KeyboardInterrupt:
    print("end \n")