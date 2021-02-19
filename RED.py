import csv
f= open("superpharmprice&name.csv",'r')
csvreader = list(csv.reader(f, delimiter=','))
print(csvreader)
SP=["Superpharm"]
SPname=[]
SPprice=[]
a=0
for i in range(1,9):
    SPname.append(csvreader[i][0])
    SPprice.append(csvreader[i][1])
for name in SPname:
    if name=="LACOSTE Red":
        SP.append(name)
        SP.append(SPprice[a])
    a = a + 1
f=open("perfumyname&price.csv", "r")
csvreader = list(csv.reader(f, delimiter=','))
print(csvreader)
P=["Perfumy"]
Pname=[]
Pprice=[]
b=0
for i in range(1,9):
    Pname.append(csvreader[i][0])
    Pprice.append(csvreader[i][1])
for name in SPname:
    if name == "Lacoste Red":
        P.append(name)
        P.append(Pprice[a])
    a = a + 1
print(SP,P)