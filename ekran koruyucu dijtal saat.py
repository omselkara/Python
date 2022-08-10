from tkinter import *
import pyautogui as pag
from time import sleep,time
import datetime
eski = 0
def kapa():
    global eski,süre
    pencere = Tk()
    pencere.attributes('-fullscreen',True)
    canvas = Canvas(pencere,width=1366,height=768,bg="black",highlightthickness=False)
    canvas.pack()
    canvas.create_rectangle(288,225,1088,525,fill="#%02x%02x%02x" % (100,153,84))
    nokta1 = canvas.create_oval(385+288,310,415+288,340,fill="#%02x%02x%02x" % (96, 146, 82),outline="#%02x%02x%02x" % (96, 146, 82))
    nokta2 = canvas.create_oval(385+288,415,415+288,445,fill="#%02x%02x%02x" % (96, 146, 82),outline="#%02x%02x%02x" % (96, 146, 82))
    sıra = 0
    eskisıra = 1
    asd = time()
    yenile = 1
    an = datetime.datetime.now()
    eskian = an
    if len(str(an.hour)) > 1:
        saat1 = int(str(an.hour)[0])
        saat2 = int(str(an.hour)[1])
    else:
        saat1 = 0
        saat2 = int(str(an.hour)[0])
    if len(str(an.minute)) > 1:
        dakika1 = int(str(an.minute)[0])
        dakika2 = int(str(an.minute)[1])
    else:
        dakika1 = 0
        dakika2 = int(str(an.minute)[0])
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 1 and saat1 != 4:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi1 = canvas.create_rectangle(339,233,450,249,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 0 and saat1 != 1 and saat1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi2 = canvas.create_rectangle(339,361,450,377,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 1 and saat1 != 4 and saat1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi3 = canvas.create_rectangle(339,489,450,504,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 1 and saat1 != 2 and saat1 != 3 and saat1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi4 = canvas.create_rectangle(322,251,338,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 1 and saat1 != 3 and saat1 != 4 and saat1 != 5 and saat1 != 7 and saat1 != 9:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi5 = canvas.create_rectangle(322,378,338,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 5 and saat1 != 6:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi6 = canvas.create_rectangle(451,251,467,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat1 != 2:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı1çizgi7 = canvas.create_rectangle(451,378,467,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 1 and saat2 != 4:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi1 = canvas.create_rectangle(522,233,633,249,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 0 and saat2 != 1 and saat2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi2 = canvas.create_rectangle(522,361,633,377,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 1 and saat2 != 4 and saat2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi3 = canvas.create_rectangle(522,489,633,504,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 1 and saat2 != 2 and saat2 != 3 and saat2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi4 = canvas.create_rectangle(505,251,521,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 1 and saat2 != 3 and saat2 != 4 and saat2 != 5 and saat2 != 7 and saat2 != 9:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi5 = canvas.create_rectangle(505,378,521,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 5 and saat2 != 6:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi6 = canvas.create_rectangle(634,251,650,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if saat2 != 2:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı2çizgi7 = canvas.create_rectangle(634,378,650,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 1 and dakika1 != 4:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi1 = canvas.create_rectangle(749,233,860,249,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 0 and dakika1 != 1 and dakika1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi2 = canvas.create_rectangle(749,361,860,377,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 1 and dakika1 != 4 and dakika1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi3 = canvas.create_rectangle(749,489,860,504,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 1 and dakika1 != 2 and dakika1 != 3 and dakika1 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi4 = canvas.create_rectangle(732,251,748,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 1 and dakika1 != 3 and dakika1 != 4 and dakika1 != 5 and dakika1 != 7 and dakika1 != 9:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi5 = canvas.create_rectangle(732,378,748,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 5 and dakika1 != 6:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi6 = canvas.create_rectangle(861,251,877,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika1 != 2:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı3çizgi7 = canvas.create_rectangle(861,378,877,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 1 and dakika2 != 4:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi1 = canvas.create_rectangle(932,233,1043,249,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 0 and dakika2 != 1 and dakika2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi2 = canvas.create_rectangle(932,361,1043,377,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 1 and dakika2 != 4 and dakika2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi3 = canvas.create_rectangle(932,489,1043,504,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 1 and dakika2 != 2 and dakika2 != 3 and dakika2 != 7:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi4 = canvas.create_rectangle(915,251,931,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 1 and dakika2 != 3 and dakika2 != 4 and dakika2 != 5 and dakika2 != 7 and dakika2 != 9:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi5 = canvas.create_rectangle(915,378,931,487,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 5 and dakika2 != 6:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi6 = canvas.create_rectangle(1044,251,1060,360,fill=a,width=0)
    a = ("#%02x%02x%02x" % (96, 146, 82))
    if dakika2 != 2:
        a = "#%02x%02x%02x" % (50, 50, 50)
    sayı4çizgi7 = canvas.create_rectangle(1044,378,1060,487,fill=a,width=0)
    while pag.position() == eski:
        an = datetime.datetime.now()
        if an.hour != eskian.hour or an.minute != eskian.minute or 1==1:
            eskian = an
            if len(str(an.hour)) > 1:
                saat1 = int(str(an.hour)[0])
                saat2 = int(str(an.hour)[1])
            else:
                saat1 = 0
                saat2 = int(str(an.hour)[0])
            if len(str(an.minute)) > 1:
                dakika1 = int(str(an.minute)[0])
                dakika2 = int(str(an.minute)[1])
            else:
                dakika1 = 0
                dakika2 = int(str(an.minute)[0])
            canvas.delete(sayı1çizgi1)
            canvas.delete(sayı1çizgi2)
            canvas.delete(sayı1çizgi3)
            canvas.delete(sayı1çizgi4)
            canvas.delete(sayı1çizgi5)
            canvas.delete(sayı1çizgi6)
            canvas.delete(sayı1çizgi7)
            canvas.delete(sayı2çizgi1)
            canvas.delete(sayı2çizgi2)
            canvas.delete(sayı2çizgi3)
            canvas.delete(sayı2çizgi4)
            canvas.delete(sayı2çizgi5)
            canvas.delete(sayı2çizgi6)
            canvas.delete(sayı2çizgi7)
            canvas.delete(sayı3çizgi1)
            canvas.delete(sayı3çizgi2)
            canvas.delete(sayı3çizgi3)
            canvas.delete(sayı3çizgi4)
            canvas.delete(sayı3çizgi5)
            canvas.delete(sayı3çizgi6)
            canvas.delete(sayı3çizgi7)
            canvas.delete(sayı4çizgi1)
            canvas.delete(sayı4çizgi2)
            canvas.delete(sayı4çizgi3)
            canvas.delete(sayı4çizgi4)
            canvas.delete(sayı4çizgi5)
            canvas.delete(sayı4çizgi6)
            canvas.delete(sayı4çizgi7)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 1 and saat1 != 4:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi1 = canvas.create_rectangle(339,233,450,249,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 0 and saat1 != 1 and saat1 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi2 = canvas.create_rectangle(339,361,450,377,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 1 and saat1 != 4 and saat1 != 7:
                    a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi3 = canvas.create_rectangle(339,489,450,504,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 1 and saat1 != 2 and saat1 != 3 and saat1 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi4 = canvas.create_rectangle(322,251,338,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 1 and saat1 != 3 and saat1 != 4 and saat1 != 5 and saat1 != 7 and saat1 != 9:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi5 = canvas.create_rectangle(322,378,338,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 5 and saat1 != 6:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi6 = canvas.create_rectangle(451,251,467,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat1 != 2:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı1çizgi7 = canvas.create_rectangle(451,378,467,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 1 and saat2 != 4:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi1 = canvas.create_rectangle(522,233,633,249,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 0 and saat2 != 1 and saat2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi2 = canvas.create_rectangle(522,361,633,377,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 1 and saat2 != 4 and saat2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi3 = canvas.create_rectangle(522,489,633,504,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 1 and saat2 != 2 and saat2 != 3 and saat2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi4 = canvas.create_rectangle(505,251,521,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 1 and saat2 != 3 and saat2 != 4 and saat2 != 5 and saat2 != 7 and saat2 != 9:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi5 = canvas.create_rectangle(505,378,521,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 5 and saat2 != 6:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi6 = canvas.create_rectangle(634,251,650,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if saat2 != 2:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı2çizgi7 = canvas.create_rectangle(634,378,650,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 1 and dakika1 != 4:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi1 = canvas.create_rectangle(749,233,860,249,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 0 and dakika1 != 1 and dakika1 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi2 = canvas.create_rectangle(749,361,860,377,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 1 and dakika1 != 4 and dakika1 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi3 = canvas.create_rectangle(749,489,860,504,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 1 and dakika1 != 2 and dakika1 != 3 and dakika1 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi4 = canvas.create_rectangle(732,251,748,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 1 and dakika1 != 3 and dakika1 != 4 and dakika1 != 5 and dakika1 != 7 and dakika1 != 9:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi5 = canvas.create_rectangle(732,378,748,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 5 and dakika1 != 6:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi6 = canvas.create_rectangle(861,251,877,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika1 != 2:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı3çizgi7 = canvas.create_rectangle(861,378,877,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 1 and dakika2 != 4:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi1 = canvas.create_rectangle(932,233,1043,249,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 0 and dakika2 != 1 and dakika2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi2 = canvas.create_rectangle(932,361,1043,377,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 1 and dakika2 != 4 and dakika2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi3 = canvas.create_rectangle(932,489,1043,504,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 1 and dakika2 != 2 and dakika2 != 3 and dakika2 != 7:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi4 = canvas.create_rectangle(915,251,931,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 1 and dakika2 != 3 and dakika2 != 4 and dakika2 != 5 and dakika2 != 7 and dakika2 != 9:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi5 = canvas.create_rectangle(915,378,931,487,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 5 and dakika2 != 6:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi6 = canvas.create_rectangle(1044,251,1060,360,fill=a,width=0)
            a = ("#%02x%02x%02x" % (96, 146, 82))
            if dakika2 != 2:
                a = "#%02x%02x%02x" % (50, 50, 50)
            sayı4çizgi7 = canvas.create_rectangle(1044,378,1060,487,fill=a,width=0)
        if time()-asd >= 0.5:
            if sıra == 0:
                sıra = 1
            else:
                sıra = 0
            asd = time()
        if sıra != eskisıra:
            canvas.delete(nokta1)
            canvas.delete(nokta2)
            yenile = 1
            eskisıra = sıra
            if sıra == 0:
                nokta1 = canvas.create_oval(385+288,310,415+288,340,fill="#%02x%02x%02x" % (96, 146, 82),outline="#%02x%02x%02x" % (96, 146, 82))
                nokta2 = canvas.create_oval(385+288,415,415+288,445,fill="#%02x%02x%02x" % (96, 146, 82),outline="#%02x%02x%02x" % (96, 146, 82))
            else:
                nokta1 = canvas.create_oval(385+288,310,415+288,340,fill="#%02x%02x%02x" % (50, 50, 50),outline="#%02x%02x%02x" % (96, 146, 82))
                nokta2 = canvas.create_oval(385+288,415,415+288,445,fill="#%02x%02x%02x" % (50, 50, 50),outline="#%02x%02x%02x" % (96, 146, 82))
        if yenile == 1:
            canvas.update()
            yenile = 0
    süre = 0
    eski = pag.position()
    pencere.destroy()
    pencere.mainloop()
süre = 0
while 1:
    if int(süre) >= 1:
        kapa()
    if not eski:
        eski = pag.position()
    if pag.position()[0] == eski[0] and pag.position()[1] == eski[1]:
        süre += 0.1
    else:
        süre = 0
        eski = pag.position()
    sleep(0.1)
