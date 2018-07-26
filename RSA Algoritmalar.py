import random
from random import randrange, getrandbits
from itertools import repeat
from functools import reduce
from datetime import datetime
import time
import sys

#
sys.setrecursionlimit(2120000000)



print("""
--------------------------------------------------------------------



                ***********************************
                   ******************************
                        RSA ANAHTAR ÜRETECİ
                      ----------------------
                          ENCRYPT-DECRYPT
                   ******************************
                ***********************************



--------------------------------------------------------------------



""")



'''
Büyük ortak Böleni Belirlemek İçin
2 Sayının Asallığını Test Etmek için Kullandık !
'''

def gcd(a,b):
    while b!=0:
        a,b=b,a%b

    return a


'''
Uzatılmış Öklid Algoritması aralarında asal 2 sayının Modüler Tersini Bulmak için 
'''

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



def modinv(a, m):
    #Buradaki a : e yi , m : phi(n) temsil etmektedir.
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modüler Ters Bulunamadı !!')
    else:
        return x % m

#Asallık Kontrolü
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def manuelanahtar(p, q):
    if p == q:
      raise ValueError('P veya Q Eşit Olmamalı')
    # n = pq
    n = (p * q)

    # Phi fonksiyonu (Totient)
    phi = (p - 1) * (q - 1)

    # E ile phi aralarında asal olacak

    e = int(input("\n\nE Değeri : (1<e<{} ve Phi(n)={} ile aralarında asal olmalı) : ".format(phi,phi)))


    # Öklid algoritmasını kullanarak Phi(n) ve e nin asallağını onaylama
    if (1 < e < phi):
      g = gcd(e, phi)
      while g != 1:
        e = int(input("E Değeri : (1<e<Phi(n)) Arasında --- ve --Phi(n) ile aralarında asal olmalı) : "))
        g = gcd(e, phi)
    elif (e > phi):
      print("E Sayısı Phi değerinden Büyük Olamaz")

    # Uzatılmış öklid algoritmasını kullanarak Gizli (Private Key bulma)
    d =modinv(e, phi)

    # Son Olarak Gizli Ve açık anahtarlarımızı çevirme
    # Açık Anahtarlar (e, n) and Gizli Anahtarlar is (d, n)
    return """

        E (Açık Anahtar) -> {}
        
        Phi Değeri -> {}

        N Değeri -> {}

        D  (Gizli Anahtar) -> {}

        """.format(e,phi, n, d)

def otoanahtar(p,q):

    # n = pq
    n = (p * q)

    # Phi fonksiyonu (Totient)
    phi = (p - 1) * (q - 1)

    e=random.randrange(1,phi)


    g=gcd(e,phi)
    while g!=1:
        e =random.randrange(1,phi)
        g=gcd(e,phi)

    d=modinv(e,phi)

    return """
    
    E (Açık Anahtar) -> {}
    
    Phi Değeri -> {}
    
    N Değeri -> {}
    
    D  (Gizli Anahtar) -> {}
    
    """.format(e,phi,n,d)


def klavyedengirilen(p, q):




    # n = pq
    n = (p * q)

    # Phi fonksiyonu (Totient)
    phi = (p - 1) * (q - 1)

    # E ile phi aralarında asal olacak


    e = int(input("\n\nE Değeri : (1<e<{} ve Phi(n)={} ile aralarında asal olmalı) : ".format(phi,phi)))

    # Öklid algoritmasını kullanarak Phi(n) ve e nin asallağını onaylama
    if (1 < e < phi):
        g = gcd(e, phi)
        while g != 1:
            e = int(input("E Değeri : (1<e<Phi(n)) Arasında --- ve --Phi(n) ile aralarında asal olmalı) : "))
            g = gcd(e, phi)
    elif (e > phi):
        print("E Sayısı Phi değerinden Büyük Olamaz")

    # Uzatılmış öklid algoritmasını kullanarak Gizli (Private Key bulma)
    d = modinv(e, phi)

    # Son Olarak Gizli Ve açık anahtarlarımızı çevirme
    # Açık Anahtarlar (e, n) and Gizli Anahtarlar is (d, n)
    return """

           E (Açık Anahtar) -> {}

           Phi Değeri -> {}

           N Değeri -> {}

           D  (Gizli Anahtar) -> {}

           """.format(e, phi, n, d)


def getPrime(n):
    

    def isProbablePrime(n, t=7):

        def isComposite(a):

            if pow(a, d,n) == 1:
            #Burada a**d % n belirtir.
                return False

            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True

        assert n > 0
        if n < 3:
            return [False, False, True][n]
        elif not n & 1:
            return False
        else:
            s, d = 0, n - 1
            while not d & 1:
                s += 1
                d >>= 1
        for _ in repeat(None, t):
            if isComposite(randrange(2, n)):
                return False
        return True

    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p





while True:
  secim = int(input("[ 1 ] : (Rastgele P,Q,E Değerlerini Üretir..) \n[ 2 ] : (Rastgele P,Q Değerleri üretir . E Anahtarı Klavyeden Girilir) \n[ 3 ] : Klavyeden (P, Q , E) Değeri Alır  \n[ 4 ] : Encrypt-Decrypt İşlemi  \n[ 5 ] : Decrypt İşlemi   \nSeçmek istenilen İşlemi Belirtin : : "))
  print("\n")
  if secim==1:
    dosya=open("otoanahtar.txt","a",encoding="utf-8")

    asal=int(input("Kaç Bitlik (P,Q) Üretilsin (En az 8 Bit ve Üzeri) : "))
    print("-----------------------------\n")

    x=getPrime(asal)
    y=getPrime(asal)
    while (x!=y):

     print("P : ",x)
     print("-----------------------------\n")
     print("Q : ",y)
     print("-----------------------------\n")
     print(otoanahtar(x,y))
     dosya.writelines("P : " + str(x))
     dosya.writelines("\nQ : " + str(y))
     dosya.writelines(str(otoanahtar(x, y)) + "\n-------------------------------------------\n")
     dosya.close()
     break

  

  elif secim==2:

      asal = int(input("Kaç Bitlik (P,Q) Üretilsin : "))

      x = getPrime(asal)
      y = getPrime(asal)
      print("P : ", x)
      print("Q : ", y)
      print(manuelanahtar(x,y))




  elif(secim==3):
      p=int(input("P Değeri : "))
      q=int(input("Q Değeri  : "))
      if(is_prime(p) and is_prime(q)):
       print(klavyedengirilen(p,q))
      elif(is_prime(p) and not is_prime(q)):
          print("\n\nQ Değeri Asal Değil Tekrar Deneyin !! \n\n")
          continue
      elif(not is_prime(p) and is_prime(q)):
          print("\n\nP değeri Asal Değil Tekrar Deneyin !! \n\n")
          continue
      else:
          print("\n\nP ve Q Asal Değil Tekrar Deneyin !!! \n\n")
          continue
  elif(secim==4):
      dosya2=open("encrypt.txt","a",encoding="utf-8")
      n=int(input("N Değerini Giriniz : "))
      e=int(input("\nE (Public Key) Giriniz : "))
      m=int(input("\nŞifrelemek İstediğiniz Mesaj (Sadece Sayısal Değerler): "))



      encrypt=pow(m,e,n)
      print("Şifrelenmiş Metin :\n\n",str(encrypt))
      dosya2.writelines("Encrypted (Metin) :\n"+str(encrypt)+"\n")
      print("--------------------------------------")
      devam=int(input("Decrypt İşlemine Devam Etmek İçin ( 4 ) e tekrar basın : "))
      if devam==4:
          d=int(input("D (Private Key Giriniz) : "))
          print("\n-----------------------------------------------------")
          decrypt=pow(encrypt,d,n)

          print("Çözümlenmiş Metin :\n"+str(decrypt))
          dosya2.writelines("\n\nDecrypt (Metin) :\n " + str(decrypt) + "\n---------------------------------------------")


      else:
          print("\n\n")
          continue
      dosya2.close()

  elif(secim==5):
      n=int(input("N değerini Giriniz : "))
      d=int(input("D (Private Key) Giriniz : "))
      cipher=int(input("Şifrelenmiş Mesajı Giriniz : "))

      decrypt=pow(cipher,d,n)
      print("Çözümlenen Mesaj :\n\n"+str(decrypt))






  else:
      print("Sadece Belirtilen İşlemleri Seçin !!!")
  continue





