from ai import network
import csvfile

#Örnek {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'setosa'}
#Dataset yükleme
iris = csvfile.load("iris.csv")
#Networku oluşturma
net = network(4,[32],3,100)
# İnput ve outputları hazırlama
inputs = []
outputs = [[],[],[]]
classes = {"setosa":[1,0,0],"versicolor":[0,1,0],"virginica":[0,0,1]}
for i in iris:
    inputs.append([float(i["sepal_length"]),float(i["sepal_width"]),float(i["petal_length"]),float(i["petal_width"])])
    for index,i in enumerate(classes[str(i["species"])]):
        outputs[index].append(i)
def test():
    doğru = 0
    yanlış = 0
    for i in iris:
        out = net.activate([float(i["sepal_length"]),float(i["sepal_width"]),float(i["petal_length"]),float(i["petal_width"])])
        if out==classes[str(i["species"])]:
            doğru += 1
        else:
            yanlış += 1
    print("Doğru Sayısı:"+str(doğru)+"\n"+"Yanlış Sayısı:"+str(yanlış))
#Eğitme
#------------------------------
#print("Eğitim")
#net.train(inputs,outputs,3)
#net.save()
#------------------------------
#Kayıt Dosyasını yükleme
net.load()
test()
while 1:
    s_l = float(input("Sepal Length:"))
    s_w = float(input("Sepal Width:"))
    p_l = float(input("Petal Length:"))
    p_w = float(input("Petal Width:"))
    out = net.activate([s_l,s_w,p_l,p_w])
    if out[0]==1:
        print("Setosa")
    elif out[1]==1:
        print("Versicolor")
    else:
        print("Virginica")
