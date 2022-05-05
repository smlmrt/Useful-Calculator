import math
import time

print("""******************
Hesap makinesi 2

işlemler
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Üs almak için
6.Sayının logaritması için
7.Küp hacmi
8.Dikdörtgenler prizması hacim
9.Koninin hacmi

******************""")

while True:
    işlem = input("İşlem seçiniz:")

    if (işlem == 'q' or işlem == 'Q'):
        print("İşleminiz sonlandırılıyor...")
        time.sleep(1)
        print("Tekrar bekleriz.")
        break

    elif (işlem == '1'):
        a = int(input("Sayı:"))
        b = int(input("Sayı:"))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} + {} = {}".format(a,b,a+b))

    elif (işlem == '2'):
        a = int(input("Sayı:"))
        b = int(input("Sayı:"))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} - {} = {}".format(a,b,a-b))

    elif (işlem == '3'):
        a = int(input("Sayı:"))
        b = int(input("Sayı:"))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} * {} = {}".format(a,b,a*b))

    elif (işlem == '4'):
        a = int(input("Sayı:"))
        b = int(input("Sayı:"))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} / {} = {}".format(a,b,a/b))

    elif (işlem == '5'):
        a = int(input("Sayının tabanını giriniz:"))
        b = int(input("Sayının üssünü giriniz:"))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        x = math.pow(a, b)
        print("{} ** {} = {}".format(a,b,math.pow(a,b)))

    elif (işlem == '6'):
        a = int(input(" sayıyı giriniz : "))
        b = int(input(" logaritmanın tabanını giriniz : "))
        print("işleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} sayısının {} tabanında logaritması = {} ".format(a,b, math.log(a,b)))

    elif (işlem == '7'):
        a = int(input("1.kenar: "))
        b = int(input("2.kenar: "))
        h = int(input("Yükseklik: "))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} * {} * {} = Küpün hacmi {} cm3 ".format(a,b,h, a*b*h))

    elif (işlem == '8'):
        a = int(input("1.kenar: "))
        b = int(input("2.kenar: "))
        h = int(input("Yükseklik: "))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} * {} * {} = Dikdörtgenler Prizmasının hacmi {} cm3 ".format(a, b, h, a*b*h))

    elif (işlem == '9'):                            # Not: koninin hacmi (1/3)π*r*r*h
        t = float(input("3 te 1 i: "))
        a = float(input("Pi sayısı : "))
        b = int(input("r: "))
        h = int(input("h: "))
        print("İşleminiz yapılmaktadır.")
        time.sleep(1)
        print("{} * {} * {} * {} * {} = koninin hacmi {} cm3".format(t, a, b, b, h,  t * a * b * b * h))

    else:
        print("Geçersiz işlem...")