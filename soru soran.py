import random
dogru = 0
yanlis = 0
while 1:
    sayi1 = int(random.uniform(0,11))
    sayi2 = int(random.uniform(0,11))
    try:
        gelen = int(input("{}x{}:".format(sayi1, sayi2)))
        islem = int(sayi1)*int(sayi2)
        cevap = eval(str(islem))
        if int(gelen) == int(cevap):
            print("\n"*50)
            print("Tebrikler doğru bildiniz")
            dogru += 1
            print("\t"*5, "Doğru sayın:{}".format(dogru), end="\t")
            print("Yanlış sayın:{}".format(yanlis))
        else:
            print("\n"*50)
            print("Malesef yanlış bildiniz")
            yanlis += 1
            print("\t"*5, "Doğru sayın:{}".format(dogru), end="\t")
            print("Yanlış sayın:{}".format(yanlis))
    except ValueError:
        print("\n"*50)
        print("Cevaba yanlızca sayı yazabilirsin")