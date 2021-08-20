import numpy as np
import pandas as pd

#küçük bir bilgi random olarak 2D array üretmek için
#print(np.random.rand(5,4))


#Seriler
sozluk={"Atil":50,"Zeynep":40,"Mehmet":30}
print(pd.Series(sozluk))

yas=[50,40,30]
isim=["Atil","Zeynep","Mehmet"]
print(pd.Series(data=yas,index=isim))

#Serilerde indexleme aynı dictionarydaki gibi mesela:
isimYasSerisi=pd.Series(data=yas,index=isim)
print(isimYasSerisi["Atil"])

#Serilerde 4 islem:Aynı indexe sahip verileri toplar diğerlerinde NaN yazar
seri1=pd.Series([10,20,30,40],["a","b","c","d"])
seri2=pd.Series([30,50,90,20],["a","x","d","z"])
print(seri1+seri2)


print("*"*30+"DataFrame"+30*"*")

"""
DataFrame Serilerin birleşmiş halidir
DataFrame de çok önemli bir özellik var bu özellik ise 
indeksleme yapacağın zaman data[0] dersen ilk satır değil
ilk sütun gelir
"""

data=np.random.randn(5,3)
dataFrame=pd.DataFrame(data,index=["Atil","Zeynep","Atlas","Mehmet","Selim"],columns=["Maas","Yas","Calisma Süresi"])
print(dataFrame)

print("\nKey ile Columnlara Erisim\n")

print(dataFrame[["Yas"]])
#Tekli column isterken (dataFrame["Yas"] yazabilirsin fakat
#Coklu columnda [["Yas","Maas"]] şeklinde yazmalısın
print()
print(dataFrame[["Yas","Maas"]])
print()

#DataFrame de herhangi bir row u istiyorsan eğer:
print(dataFrame.loc["Atil"])
#şeklinde yazmalısın
print()
#Columnu almanın diğer bir yolu ise 
print(dataFrame.iloc[[0,1]]) #iloc yani index bazlı location
#yaparak ilk iki row getirebilirsin 

print()
dataFrame["Emeklilik Yasi"]=dataFrame["Yas"]+dataFrame["Yas"]
print(dataFrame)
print()
dataFrame.drop("Emeklilik Yasi",axis=1,inplace=True)
print(dataFrame)
print()
dataFrame.drop("Atil",axis=0,inplace=True)
print(dataFrame)
print(dataFrame.loc["Zeynep","Maas"])
print(dataFrame.loc["Zeynep"]["Maas"])
print()
print(dataFrame[dataFrame["Maas"]>0])
print()

havaDurumuSozluk={"İstanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"İzmir":[40,39,38]}
havaDurumuDataFrame=pd.DataFrame(havaDurumuSozluk)
print(havaDurumuDataFrame)
print(havaDurumuDataFrame.dropna())
print(havaDurumuDataFrame)
print(havaDurumuDataFrame.dropna(axis=1))

yeniVeri={"İstanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"İzmir":[40,39,38],"Antalya":[45,np.nan,np.nan]}
yeniDataFrame=pd.DataFrame(yeniVeri)
print(yeniDataFrame)
print(yeniDataFrame.dropna(axis=1,thresh=2))#thresh demek sınır demek
print(yeniDataFrame.fillna(-5))

print(50*"*")
maasSozlugu={
    "Departman":["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
    "Calisan Ismi":["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
    "Maas":[100,150,200,300,400,500]
}
maasDataFrame=pd.DataFrame(maasSozlugu)
print(maasDataFrame)
print(maasDataFrame.groupby("Departman"))
print(maasDataFrame.groupby("Departman").count())
print(maasDataFrame.groupby("Departman").mean())
print(maasDataFrame.groupby("Departman").sum())
print(maasDataFrame.groupby("Departman").describe())
print(maasDataFrame.groupby("Departman").min())


print(dataFrame)
dataFrame["Calisma Süresi"]=dataFrame["Calisma Süresi"]*5
print(dataFrame)


