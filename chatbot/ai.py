import json
import random
from copy import deepcopy
class network:
    def __init__(self):
        self.words = []
        self.fitnesses = []
        self.classes = []
        self.cevaplar = []
        self.best = float("-inf")
    def train(self,name,pop,epoch):
        texts,classes,self.classes,self.cevaplar = gettext(name)
        words = generatewords(texts)
        self.words = deepcopy(words)
        genomes = []
        for i in range(pop):
            genomes.append(genome(words,classes))
        for _ in range(epoch):
            yer = 0
            best = float("-inf")
            for i in range(pop):
                fitness = 0
                for out in range(len(texts)):
                    if genomes[i].activate(texts[out])==classes[out]:
                        fitness += 1
                if fitness>best:
                    best = fitness
                    yer = i
            clone = genomes[yer].get_clone()
            print(f"Epoch:{_}   Acc:%{best*100/len(classes)}")
            if _!=epoch-1:
                for i in range(pop):
                    genomes[i].set_clone(clone)
                    genomes[i].mutate()
            if best>self.best:
                self.best = best
                self.fitnesses = deepcopy(clone)
    def save(self,name="network.json"):
        data = {}
        data["words"] = self.words
        data["fitnesses"] = self.fitnesses
        data["classes"] = self.classes
        data["cevaplar"] = self.cevaplar
        data["best"] = self.best
        with open(name, 'w',encoding="utf-8") as json_file:
            json.dump(data, json_file)
    def load(self,name="network.json"):
        with open(name,encoding="utf-8") as f:
            data = json.load(f)
        self.words = data["words"]
        self.fitnesses = data["fitnesses"]
        self.classes = data["classes"]
        self.cevaplar = data["cevaplar"]
        self.best = data["best"]
    def activate(self,text):
        words = text.lower().split(" ")
        outs = []
        for i in range(len(self.fitnesses[0])):
            outs.append(0)
        varmı = False
        for i in words:
            try:
                points = self.fitnesses[self.words.index(i)]
                for index,a in enumerate(points):
                    outs[index] += a
                varmı = True
            except:
                print(f'"{i}" ne demek bilmiyorum')
        out = outs.index(max(outs))
        cevaplar = self.cevaplar[out]
        for i in range(len(outs)):
            print(f"{self.classes[i]} Puanı:{outs[i]}")
        print()
        print(f"Bulduğum anlam:{self.classes[out]}")
        print()
        if varmı:
            return cevaplar[random.randint(0,len(cevaplar)-1)]
        else:
            return ""
class genome:
    def __init__(self,words,classes):
        self.words = []
        self.fitnesses = []
        classlen = max(classes)+1
        for i in words:
            self.words.append(i)
            self.fitnesses.append([])
            for a in range(classlen):
                self.fitnesses[-1].append(random.uniform(-10,10))
    def activate(self,text):
        words = text.lower().split(" ")
        outs = []
        for i in range(len(self.fitnesses[0])):
            outs.append(0)
        for i in words:
            try:
                points = self.fitnesses[self.words.index(i)]
                for index,a in enumerate(points):
                    outs[index] += a
            except:
                pass
        return outs.index(max(outs))
    def get_clone(self):
        return deepcopy(self.fitnesses)
    def set_clone(self,fitnesses):
        self.fitnesses = deepcopy(fitnesses)
    def mutate(self):
        for i in range(len(self.fitnesses)):
            for a in range(len(self.fitnesses[i])):
                if random.uniform(0,100)<5:
                    self.fitnesses[i][a] += random.uniform(-1,1)
                elif random.uniform(0,100)<1:
                    self.fitnesses[i][a] = random.uniform(-10,10)
def generatewords(texts):
    words = []
    for i in texts:
        for a in i.lower().split(" "):
            if not a in words:
                words.append(a)
    return words
def gettext(name):
    with open(name,encoding="utf-8") as f:
        data = json.load(f)
    texts = []
    outs = []
    classes = []
    cevaplar = []
    for i in range(len(data["texts"])):
        cevaplar.append([])
        classes.append(data["texts"][i]["tag"])
        for a in data["texts"][i]["sorular"]:
            texts.append(a)
            outs.append(i)
        for a in data["texts"][i]["cevaplar"]:
            cevaplar[-1].append(a)
    return texts,outs,classes,cevaplar
