def bittopla(bit1,bit2,hand):
    value = "0"
    elde = "0"
    if bit1=="0":
        if bit2=="0":
            if hand=="0":
                pass
            else:
                value = "1"
        else:
            if hand=="0":
                value = "1"
            else:
                elde = "1"
                
    else:
        if bit2=="0":
            if hand=="0":
                value = "1"
            else:
                elde = "1"
        else:
            if hand=="0":
                elde = "1"
            else:
                value = "1"
                elde = "1"
    return [value,elde]

def topla(sayı1,sayı2):
    result = ["0" for i in range(max(len(sayı1),len(sayı2)))]
    elde = "0"
    if len(sayı1)>len(sayı2):
        sayı2 = (len(sayı1)-len(sayı2))*"0"+sayı2
    elif len(sayı2)>len(sayı1):
        sayı1 = (len(sayı2)-len(sayı1))*"0"+sayı1
    for index in reversed(range(max(len(sayı1),len(sayı2)))):
        value,elde = bittopla(sayı1[index],sayı2[index],elde)
        result[index] = value
    if elde=="1":
        result.insert(0,"1")
    return "".join(result)

def floattopla(sayı1,sayı2):
    intsayı1 = int(sayı1)
    intsayı2 = int(sayı2)
    floatsayı1 = int(str(sayı1)[str(sayı1).index(".")+1::])
    floatsayı2 = int(str(sayı2)[str(sayı2).index(".")+1::])    
    maxlength = max(len(str(sayı1)[str(sayı1).index(".")+1::]),len(str(sayı2)[str(sayı2).index(".")+1::]))
    floatsayı1 *= 10**(maxlength-len(str(sayı1)[str(sayı1).index(".")+1::]))
    floatsayı2 *= 10**(maxlength-len(str(sayı2)[str(sayı2).index(".")+1::]))
    floatresult = int(topla(str(bin(floatsayı1))[2::],str(bin(floatsayı2))[2::]),2)
    intresult = intsayı1+intsayı2
    if len(str(floatresult))>maxlength:
        intresult += int(str(floatresult)[0])
        floatresult = int(str(floatresult)[1::])
    return float(str(intresult)+"."+str(floatresult))
    
    
print(floattopla(0.1,0.000022))

