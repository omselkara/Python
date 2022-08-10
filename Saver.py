num_range = 4

def turn_readable(n):
    return "0"*(num_range-len(str(n)))+str(n)
    
def load(name):
    file = open(name,"r",encoding="utf-8")
    file = file.readlines()
    liste = []
    for i in file:
        if "\n" in i:
            liste.append(i[0:-1])
        else:
            liste.append(i)
    text = ""
    for i in liste:
        text += i
    file = decode(text)
    return eval(f"{file}")

def decode(file):
    text = ""
    for s in range(0,len(file),num_range):
        text += chr(int(file[s:s+num_range]))
    return text

def encode(texts):
    liste = []
    text = ""
    for s in texts:
        text += turn_readable(ord(s))
        if len(text)==200:
            liste.append(text)
            text = ""
    if text!="":
        liste.append(text)
    return liste

def save(name,texts):
    file = open(name,"w",encoding="utf-8")
    if type(texts)!=str:
        texts = encode(str(texts))
    else:
        texts = encode(texts)
    for i in texts:
        file.write(i+"\n")
    file.close()


