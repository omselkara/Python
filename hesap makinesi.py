olmalı = "1234567890*-/+"
while 1:
    gelen = input("Yapacağınız işlemi yazın:")
    for sayı in gelen:
        if sayı not in olmalı:
            print("Neyin peşindesin\n",len("Neyin peşindesin")*"-", sep="")
            break
        else:
            try:
                if len(str(eval(gelen))) > 167:
                    print(eval(gelen), '\n', 167*"-", sep="")
                    break
                print(eval(gelen), '\n', len(str(eval(gelen)))*"-", sep="")
                break
            except ZeroDivisionError:
                print("Hiçbirşeyi 0 a bölemezsin")
                break
