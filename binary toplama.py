def topla(sayı1,sayı2):
    liste = []
    sayı1 = int(bin(sayı1)[2:])
    sayı2 = int(bin(sayı2)[2:])
    if len(str(sayı1)) > len(str(sayı2)):
        uzunluk = len(str(sayı1))+1
    else:
        uzunluk = len(str(sayı2))+1
    if len(str(sayı1))+1 != uzunluk:
        sayı1 = "{}{}".format("0"*((uzunluk-1)-len(str(sayı1))),sayı1)
    if len(str(sayı2))+1 != uzunluk:
        sayı2 = "{}{}".format("0"*((uzunluk-1)-len(str(sayı2))),sayı2)
    elde = 0
    for i in range(1,uzunluk):
        if i != uzunluk-1:
            if int(str(sayı1)[-i]) == 1 and int(str(sayı2)[-i]) == 1:
                if elde == 1:
                    liste.insert(-i,"1")
                else:
                    liste.insert(-i,"0")
                    elde = 1
            if int(str(sayı1)[-i]) == 0 and int(str(sayı2)[-i]) == 0:
                if elde == 1:
                    liste.insert(-i,"1")
                    elde = 0
                else:   
                    liste.insert(-i,"0")
                    elde = 0
            if int(str(sayı1)[-i]) == 1 and int(str(sayı2)[-i]) == 0:
                if elde == 1:
                    liste.insert(-i,"0")
                    elde = 1
                else:
                    liste.insert(-i,"1")
                    elde = 0
            if int(str(sayı1)[-i]) == 0 and int(str(sayı2)[-i]) == 1:
                if elde == 1:
                    liste.insert(-i,"0")
                    elde = 1
                else:
                    liste.insert(-i,"1")
                    elde = 0
        else:
            if int(str(sayı1)[-i]) == 1 and int(str(sayı2)[-i]) == 1:
                if elde == 1:
                    liste.insert(-i,"1")
                    liste.insert(0,"1")
                else:
                    liste.insert(-i,"0")
                    liste.insert(0,"1")
            if int(str(sayı1)[-i]) == 0 and int(str(sayı2)[-i]) == 0:
                if elde == 1:
                    liste.insert(-i,"1")
                else:   
                    liste.insert(-i,"0")
            if int(str(sayı1)[-i]) == 1 and int(str(sayı2)[-i]) == 0:
                if elde == 1:
                    liste.insert(-i,"0")
                    liste.insert(0,"1")
                else:
                    liste.insert(-i,"1")
                    elde = 0
            if int(str(sayı1)[-i]) == 0 and int(str(sayı2)[-i]) == 1:
                if elde == 1:
                    liste.insert(-i,"0")
                    liste.insert(0,"1")
                else:
                    liste.insert(-i,"1")
                    elde = 0
    sayı = str(liste[0])
    for i in range(1,len(liste)):
        sayı = str(sayı)+str(liste[i])
    sayı = int(sayı,2)
    return int(sayı)
