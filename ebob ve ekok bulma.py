while 1:
        sayı1 = int(input("İlk sayıyı giriniz:"))
        sayı2 = int(input("İkinci sayıyı giriniz:"))
        sayaç1 = 1
        sayaç2 = 1
        çarpan1 = []
        çarpan2 = []
        ebob = 0
        def çarpan_bul(sayaç, sayı, çarpan):
                while 1:
                        if sayaç > sayı:
                                break
                        if sayı % sayaç == 0:
                                çarpan.append(sayaç)
                        sayaç += 1
        çarpan_bul(sayaç1, sayı1, çarpan1)
        çarpan_bul(sayaç2, sayı2, çarpan2)
        for i1 in çarpan1:
                for i2 in çarpan2:
                        if i1 == i2 and i2 > ebob:
                                ebob = i2
        #EBOB X EKOK = sayı1 X sayı2
        if ebob == 1:
                print("{} ve {} sayıları aralarında asaldır".format(sayı1, sayı2))
        else:
                print("{} ve {} sayılarının ebobu {}".format(sayı1, sayı2, ebob))
        ekok = int((sayı1*sayı2)/ebob)
        print("{} ve {} sayılarının ekoku {}".format(sayı1, sayı2, ekok))
                        
        
        
        
        
