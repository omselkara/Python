import random
from time import sleep
import datetime
cevap_liste = []
an1 = datetime.datetime.now()
deneme = 0
for i in range(6):
    liste = []
    gerçek_cevap = 5 ** 0.5
    ortalama = 0
    küçük = 0
    büyük = 2
    bitme = 0
    bulunanlar = []
    for i in range(1001):
        a = random.uniform(40,60)
        a = round(a,4)
        liste.append(a)
    a = random.uniform(0,2)
    while abs(gerçek_cevap-ortalama) != 0 :
        ekle = 0.0001
        if gerçek_cevap-ortalama < 0:
            a -= ekle
        if gerçek_cevap-ortalama > 0:
            a += ekle
        ortalama = 0
        for i in liste:
            ortalama += i*a
        ortalama = ortalama/len(liste)
        for i in bulunanlar:
            if i == ortalama and i >= gerçek_cevap :
                bitme = 1
                cevap_liste.append(i)
                break
        if bitme == 1:
            break
        bulunanlar.append(ortalama)
        deneme += 1
sayı1 = []
sayı2 = []
sayı3 = []
sayı4 = []
sayı5 = []
ortak = []
for i in str(cevap_liste[0]):
    sayı1.append(i)
for i in str(cevap_liste[1]):
    sayı2.append(i)        
for i in str(cevap_liste[2]):
    sayı3.append(i)
for i in str(cevap_liste[3]):
    sayı4.append(i)
for i in str(cevap_liste[4]):
    sayı5.append(i)
uzunluk = len(sayı1)
for i in range(0, uzunluk-1):
    if sayı1[i] == sayı2[i] and sayı1[i] == sayı3[i] and sayı1[i] == sayı4[i] and sayı1[i] == sayı5[i]:
        try:
            if sayı1.index(sayı1[i]) != ortak.index(ortak[len(ortak)-1]):
                for a in range(1, sayı1.index(sayı1[i])-ortak.index(ortak[len(ortak)-1])):
                    ortak.append("0")
        except:
            pass
        ortak.append(sayı1[i])
an2 = datetime.datetime.now()
süre = an2 - an1
dakika = str(süre)[2:4]
saniye = str(süre)[5:7]
milisaniye = str(süre)[8:]
print("Cevap yaklaşık:",end="")
for i in ortak:
    print(i,end="")
print("")
print("{} Sayıda deneme ile {} Dakika {} Saniye {} Milisaniyede buldum".format(deneme, dakika, saniye, milisaniye))
a = input("")
