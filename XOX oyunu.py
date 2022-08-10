tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]
kişi1 = input("X kim:")
kişi2 = input("0 kim:")
kişi1 = kişi1.title()
kişi2 = kişi2.title()
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)

kazanma = [[[0, 0], [0, 1], [0, 2]],
           [[1, 0], [1, 1], [1, 2]],
           [[2, 0], [2, 1], [2, 2]],
           [[0, 0], [1, 0], [2, 0]],
           [[0, 1], [1, 1], [2, 1]],
           [[0, 2], [1, 2], [2, 2]],
           [[0, 0], [1, 1], [2, 2]],
           [[0, 2], [1, 1], [2, 0]]]
    
x_durumu = []
o_durumu = []

sıra = 1
while 1:
    if sıra %2 == 0:
        işaret = "0"
        
    else:
        işaret = "X"
    print()
    print("İşaret {}".format(işaret))

    x = input("Yukarıdan aşağıya doğru kaçıncı([1],[2],[3]):")
    x = int(x)-1
    y = input("Soldan sağa doğru kaçıncı([1],[2],[3]):")
    y = int(y)-1

    if tahta[x][y] == "___":
        tahta[x][y] = işaret.center(3)
        if tahta[x][y] == "X".center(3):
            x_durumu += [[x, y]]
        else:
            o_durumu += [[x, y]]
        sıra += 1
    else:   
        print("\nOrası dolu\n")
    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)

    for i in kazanma:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        print(x)
        if len(x) == len(i):
            print("{} kazandı".format(kişi1))
            çıkma = str(input("Çıkmak için kerhangi bir şeye bas"))
            quit()
        elif len(o) == len(i):
            print("{} kazandı".format(kişi2))
            çıkma = str(input("Çıkmak için herhangi bir şeye bas"))
            quit()
        elif int(sıra) == 10:
            print("Kimse kazanamadı")
            gelen =input("çıkmak için herhangi bir şeye bas")
            quit()    
        
