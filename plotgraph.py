import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplot
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from itertools import groupby
data = open("diabetes.data", "r")
datalist = []
Pregnancy= []
Plasmag = []
DBloodP = []
Triceps = []
Sinsulin = []
BodyMI = []
DiabetesPF = []
Age = []
Diabetes = []
nonDiabetes = []
AgesDBP = []
AgesDBPind = []
Indexofage= []
Pregnancy1 = []
maxpregnancyind = []
minpregnancyind = []
maxp = []
diaAge = []
years = []
years1 = []
ndiaAge = []
bos = []
bos1 = []
for i in data.readlines():
    datalist.append(i.strip("\n").split(";"))

for i in range(len(datalist)):
    Pregnancy.append(datalist[i][0])
    Plasmag.append(datalist[i][1])
    DBloodP.append(datalist[i][2])
    Triceps.append(datalist[i][3])
    Sinsulin.append(datalist[i][4])
    BodyMI.append(datalist[i][5])
    DiabetesPF.append(datalist[i][6])
    Age.append(int(datalist[i][7]))
    if datalist[i][8] == "1":
        Diabetes.append(i)
    else:    
        nonDiabetes.append(i)

for i in range(len(DBloodP)):
    if int(DBloodP[i]) >= 90:
        AgesDBP.append(Age[i])
        Indexofage.append(i)
for i in range(1,len(AgesDBP)+1):
    AgesDBPind.append(i)

for i in Indexofage:
    Pregnancy1.append(int(Pregnancy[i]))
for i in range(len(Pregnancy1)):
    if Pregnancy1[i] == max(Pregnancy1):
        maxpregnancyind.append(i)
    elif Pregnancy1[i] == 1:
        minpregnancyind.append(i)
for i in maxpregnancyind:
    maxp.append(max(Pregnancy1)/AgesDBP[i])
lol = AgesDBP[maxpregnancyind[maxp.index(max(maxp))]]

plt.xticks(np.arange(min(AgesDBPind), max(AgesDBPind)+1, 5.0))
plt.plot(AgesDBPind,AgesDBP,'b',label = "Instances")
plt.xlabel("Instances")
plt.ylabel("Ages")
plt.savefig("fig1.pdf") 

for i in Diabetes:
    diaAge.append(Age[i])
for i in nonDiabetes:
    ndiaAge.append(Age[i])  
z = sorted(ndiaAge)
z.reverse()
f = [len(list(group)) for key, group in groupby(z)]  
x = sorted(diaAge)
x.reverse()
y = [len(list(group)) for key, group in groupby(x)]

for i in z:
    years.append(str(2017-i))

for i in x:
    years.append(str(2017-i))
    

years = sorted(list(set(years)))
years1 = sorted(list(set(years1)))

x = list(set(x))
z = list(set(z))
f.insert(2,0)
y.insert(0,0)
y.insert(1,0)
y.insert(3,0)
y.insert(4,0)
y.insert(7,0)
y.insert(8,0)
y.insert(9,0)
width = 0.14
for i in range(1,len(y)+1):
    bos.append(i)
for i in range(1,len(y)+1):
    bos1.append(i-width)
pyplot.clf()
plt.bar(bos1, y,width, color = "b", label = "Diabete")
plt.bar(bos, f,width, color = "r", label = "Not-Diabete")
plt.xticks(bos,years,fontsize = 6,rotation = "65")
plt.xlabel("Years")
plt.ylabel("# of patients")
plt.legend(loc=2,prop={'size': 9})
plt.savefig(f"fig2.pdf") 

