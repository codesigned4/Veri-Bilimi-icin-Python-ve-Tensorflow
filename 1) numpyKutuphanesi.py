import numpy as np

#Numpy array
print("Numpy array")
dizi=np.array((3,4))
print(dizi.shape)

#arange methodu (normal range mothodunun numpy de kullanılışı)
print("arange methodu")
result=np.arange(0,10)
print(result)

#linspace methodu  start,stop,kaç adet
print("linspace methodu")

result=np.linspace(0,20,500)
print(result)

#random methodu 
print("random methodu")
result=np.random.randn(4)
result=np.random.randn(4,4)
result=np.random.randint(1,40)
result=np.random.randint(1,40,5)
print(result)

#indexleme
print("indexleme")
result=np.arange(0,15)
print(result[5])
result2=result
print(result2)
print(result[3:8])
result[3:8]=-5
print(result)
print(result2)
"""
numpy de ilginç olan bir özelliklerden birisi de
yukarıdaki gösterdiğim gibi result un belli bir aralığındaki sayıları değiştirmeme rağmen onu atadığım result2 nin de o indexlerindeki sayılar değşti
reference type gibi davrandı 
eğer bu şekilde olmasını istemiyorsan,valularını almak istiyorsan result2=result.copy() methodunu kullanmalısın
"""
#reshabpe methodu
print("reshabpe methodu")
result=np.arange(0,100,5)
result=result.reshape(5,4)
print(result[0,0])

#numpy ile operasyonlar
print("Numpy İle Operasyonlar")
rastgeleDizi=np.random.randint(1,100,20)
print(rastgeleDizi)
print(rastgeleDizi>20)#şeklinde tüm diziyi True False olarak karşılaşıtrabilirisin
print(rastgeleDizi[rastgeleDizi>20])
print(rastgeleDizi+rastgeleDizi)
print(rastgeleDizi-rastgeleDizi)
print(rastgeleDizi*rastgeleDizi)
print(np.max(rastgeleDizi))
print(np.min(rastgeleDizi))
print(np.sqrt(rastgeleDizi))
