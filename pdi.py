import pydirectinput as pdi
from winsound import Beep
from Control import *
import time
import keyboard
import pyautogui as pag
import numpy as np
from PIL import ImageGrab,Image
from copy import deepcopy

def wait():
    Beep(1000,1000)
    while True:
        if keyboard.read_key() == "q":
            Beep(1000,1000)
            break
def click(pos):
    x,y = pos[0],pos[1]
    pdi.moveTo(x-1,y-1)
    pdi.moveRel(1,1)
    pdi.click()
def weight():
    sat = (1320,293)
    güçbutton = (88, 261)
    güç = (563, 629)
    dayanık = (819, 622)
    rebirt = (84, 317)
    al = (685, 617)
    onay = (688, 543)
    boş = (660, 736)
    wait()
    time.sleep(1)
    while 1:
        click(sat)
        click(güçbutton)
        an = time.time()
        while 1:
            if keyboard.is_pressed("q"):
                wait()
                time.sleep(1)
                break
            else:
                if time.time()-an >= 15:
                    break
                else:
                    click(boş)
                    click(güç)
                    click(dayanık)
        for i in range(0,2):
            click(boş)
        click(rebirt)
        time.sleep(0.5)
        click(al)
        time.sleep(0.5)
        click(onay)
        time.sleep(2)
def lift():
    while 1:
        wait()
        kontrol = (549, 706)
        while 1:
            if pdi.position()[0] == 0 and pdi.position()[1] == 0:
                break
            try:
                if pag.pixel(kontrol[0],kontrol[1]) != (90, 142, 233):
                    pdi.press("1")
            except:
                pass
def dlive():
    konum = (1092,585)
    konum2 = (1156,579)
    wait()
    Beep(1000,1000)
    while 1:
        ekran = np.array(ImageGrab.grab())
        renk = ekran[konum[1]][konum[0]]
        renk2 = ekran[konum2[1]][konum2[0]]
        if renk[0] == 107 and renk[1] == 214 and renk[2] == 214 and renk2[0] == 107 and renk2[1] == 214 and renk2[2] == 214:
            pag.click(konum[0],konum[1])
def bee():
    keyboard.wait("q")
    ara = 110
    while 1:
        try:
            img = np.array(ImageGrab.grab())
            yer = img[5][960]
            if (abs(yer[0]-ara)+abs(yer[1]-ara)+abs(yer[2]-ara))>50:
                Beep(1000,500)
        except:
            pass
        time.sleep(1)
def piano():
    keyboard.wait("q")
    clicked = 0
    while 1:
        kere = 0
        for i in range(4):
            if sum(pag.pixel(525+75*i,300))/3<25:
                pag.click(525+75*i,300+clicked/40)
                clicked += 1
                kere += 1
        if kere>1:
            for i in range(4):
                if sum(pag.pixel(525+75*i,420))/3<25:    
                    pag.click(525+75*i,420)
def blastof():
    wait()
    sat = (180,320)
    topla = (920,650)
    while 1:
        click(sat)
        time.sleep(1)
        pdi.keyDown("s")
        time.sleep(0.3)
        pdi.keyUp("s")
        time.sleep(0.5)
        pdi.keyDown("a")
        time.sleep(1)
        pdi.keyUp("a")
        time.sleep(0.5)
        pdi.keyDown("w")
        time.sleep(5)
        pdi.keyUp("w")
        an = time.time()
        while 1:
            if time.time()-an>60:
                break
            click(topla)
            time.sleep(1)
def fnf():
    wait()
    h = 630
    while 1:
        for i in range(4):
            x = 585+i*90
            if pag.pixel(x,h)!=(222,232,235):
                pag.click(x,h)
def speed():
    pc = PC()
    while 1:
        wait()
        if keyboard.is_pressed("4"):
            while 1:
                pdi.keyDown("e")
                time.sleep(1)
                pdi.keyUp("e")
                an = time.time()
                while 1:
                    if time.time()-an>60 or keyboard.is_pressed("p"):
                        break
                    click([713,713])
                if keyboard.is_pressed("p"):
                    break
                time.sleep(0.1)
                while 1:
                    try:
                        col = pag.pixel(1028,200)
                        if col[0]!=255 or col[1]!=53 or col[2]!=93:
                            click([713,713])
                        break
                    except:
                        pass
                time.sleep(0.1)
                click([1004,200])
                time.sleep(0.1)
                click([72, 413])
                time.sleep(0.1)
                an = time.time()
                while 1:
                    if time.time()-an>5 or keyboard.is_pressed("p"):
                        break
                    click([553,798])
                time.sleep(0.1)
                click([1091,180])
        else:
            e = 1
            if keyboard.is_pressed("2"):
                e = 2
            elif keyboard.is_pressed("3"):
                e = 3
            pos = pc.get_pos()
            col1 = (244, 255, 255)
            col2 = (190, 218, 246)
            pdi.keyUp("s")
            pdi.keyUp("w")
            while 1:
                ok = False
                for i in range(e):
                    if keyboard.is_pressed("p"):
                        ok = True
                        break
                    pdi.press("e")
                if ok:
                    break
                pdi.keyDown("s")
                time.sleep(1)
                an = time.time()
                while 1:
                    if pc.is_down("p") or time.time()-an>30:
                        break
                    col = pc.get_pixel(pos[0],pos[1])
                    if (abs(col[0]-col1[0])+abs(col[1]-col1[1])+abs(col[2]-col1[2]))<75:
                        break
                pdi.keyUp("s")
                if time.time()-an>30:
                    while not keyboard.is_pressed("p"):
                        Beep(1000,500)
                        time.sleep(0.5)
                    break
                pc.key_down("w")
                time.sleep(1)
                an = time.time()
                while 1:
                    if pc.is_down("p") or time.time()-an>30:
                        break
                    col = pc.get_pixel(pos[0],pos[1])
                    if (abs(col[0]-col2[0])+abs(col[1]-col2[1])+abs(col[2]-col2[2]))<75:
                        print(col,col2,(abs(col[0]-col2[0])+abs(col[1]-col2[1])+abs(col[2]-col2[2])))
                        break
                pc.key_up("w")
                if time.time()-an>30:
                    while not keyboard.is_pressed("p"):
                        Beep(1000,500)
                        time.sleep(0.5)
                    break
            
def islands():
    pc = PC()
    while 1:
        pc.wait("q",1000)
        pc.key_down("a")
        pc.key_down(42)
        while not pc.is_down("p"):
            pc.add_pos(10,0)
            time.sleep(0.000001)
            pc.mouse_event()
        pc.key_up("a")
        pc.key_up(42)
def pet():
    pc = PC()
    while 1:
        pc.wait("q",100)
        if pc.is_down("1"):
            pos = (586, 581)
            while not pc.is_down("p"):
                pc.press("e")
                pc.set_pos(pos[0],pos[1])
                pc.add_pos(+1,+1)
                pc.add_pos(-1,-1)
                pc.mouse_event()
                time.sleep(0.5)
        else:
            pos = pc.get_pos()
            while not pc.is_down("p"):
                pc.set_pos(pos[0],pos[1])
                pc.mouse_event("left_down")
                time.sleep(1)
                pc.mouse_event("left_up")
def ytb():
    pc = PC()
    colors = [[110,247,111],[138,221,112],[169,193,112],[199,165,113],[231,136,114]]
    def click(x,y):
        pc.set_pos(x,y)
        pc.add_pos(+1,+1)
        pc.add_pos(-1,-1)
        pc.mouse_event()
    while 1:
        pc.wait("q",1000)
        while not pc.is_down("p"):
            pc.set_pos(1000,500);
            pc.add_pos(1,1)
            pc.add_pos(-1,-1)
            img = np.array(ImageGrab.grab())
            if (abs(img[775][720][0]-255)+abs(img[775][720][1]-254)+abs(img[775][720][2]-237))<20:
                pc.press("1")
            while 1:
                img = np.array(ImageGrab.grab())
                if pc.is_down("p") or (img[550][900][0]==0 and img[550][900][1]==103 and img[550][900][2]==103):
                    break                
                ok = False
                for y in range(250,750,30):
                    for x in range(310,1300,30):
                        for i in range(0,5):
                            if (abs(colors[i][0]-img[y][x][0])+abs(colors[i][1]-img[y][x][1])+abs(colors[i][2]-img[y][x][2]))<15:
                                click(x,y)
                                ok = True
                                break
                        if ok:
                            break
                    if ok:
                        break
                time.sleep(0.0001)
                click(1000,450)
            time.sleep(1)
            if pc.is_down("p"):
                break
            click(725,560)
            time.sleep(3)
            if pc.is_down("p"):
                break
            if pc.is_down("p"):
                break
            time.sleep(1)
            pc.key_down("w")
            time.sleep(1)
            pc.key_up("w")
            if pc.is_down("p"):
                break
            last = time.time()
            while 1:
                img = np.array(ImageGrab.grab())
                if pc.is_down("p") or (img[300][125][0]==255 and img[300][125][1]==254 and img[300][125][2]==237):
                    break                
                ok = False
                for y in range(250,750,30):
                    for x in range(310,1300,30):
                        for i in range(0,5):
                            if (abs(colors[i][0]-img[y][x][0])+abs(colors[i][1]-img[y][x][1])+abs(colors[i][2]-img[y][x][2]))<15:
                                click(x,y)
                                last = time.time()
                                ok = True
                                break
                        if ok:
                            break
                    if ok:
                        break
                time.sleep(0.0001)
                click(1000,450)
                if time.time()-last>5:
                    while not pc.is_down("p"):
                        Beep(1000,1000)
                    break
            if pc.is_down("p"):
                break
            time.sleep(1)
            if pc.is_down("p"):
                break
            click(125,850)
            time.sleep(3)
            if pc.is_down("p"):
                break
            pc.key_down("w")
            time.sleep(1)
            pc.key_up("w")

def fighter():
    pc = PC()
    pos = (720, 841)
    while 1:
        pc.wait("1",100)
        while not pc.is_down("2"):
            pc.set_pos(pos[0],pos[1])
            pc.add_pos(+1,+1)
            pc.add_pos(-1,-1)
            pc.mouse_event()
            time.sleep(0.01)


def ytbx():
    pc = PC()
    while 1:
        pc.wait("q",100)
        while not pc.is_down("p"):
            pc.click()
            pc.press("e")
            time.sleep(0.01)
            
        
def goal():
    pc = PC()
    süre = 0.511836051940918
    while 1:
        Beep(1000,100)
        pc.wait("r")
        while not pc.is_down("p"):
            pc.key_down("q")
            time.sleep(süre)
            pc.key_up("q")
            time.sleep(10)
    
def sword():
    pc = PC()
    listetuş = ["a","d","w"]
    listeyer = [[576,757],[864,757],[721,614]]
    listerenk = [[127,162,66],[145,173,77],[165,186,80]]
    while 1:
        Beep(1000,100)
        pc.wait("q")
        while not pc.is_down("p"):
            img = np.array(ImageGrab.grab())
            for i in range(3):
                pix = img[listeyer[i][1]][listeyer[i][0]]
                if pix[0] != listerenk[i][0] or pix[1] != listerenk[i][1] or pix[2] != listerenk[i][2]:
                    pc.press(listetuş[i])
            

def rugby():
    pc = PC()
    süre = 0.4139730930328369
    while 1:
        Beep(1000,100)
        pc.wait("q")
        while not pc.is_down("p"):
            pc.key_down(" ")
            time.sleep(süre)
            pc.key_up(" ")

def strong():
    pc = PC()
    while 1:
        Beep(1000,100)
        pc.wait("q")
        while not pc.is_down("p"):
            click((600,750))
            img = np.array(ImageGrab.grab())
            pix = img[583][248]
            if pix[0]==255 and pix[1]==88 and pix[2]==55:
                time.sleep(0.5)
                click((220,600))
                time.sleep(2)
                click((727,558))
                time.sleep(0.5)
                click((988,245))
                time.sleep(1)
                
            
            
def tower():
    pc = PC()
    while 1:
        Beep(1000,100)
        pc.wait("q")
        while not pc.is_down("p"):
            pc.click()
            time.sleep(0.1)

tower()


