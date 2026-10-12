print("Basit Hesap Makinesi")

sayi1 = float(input("birinci sayiyi giriniz: "))
islem = input("islem sec (+,-,*,/): ")
sayi2 = float(input("ikinci sayiyi giriniz: "))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 ==0:
        print("bir sayi sifira bolunemez.")
    else:
        sonuc = sayi1 / sayi2
else:
    print("gecersiz islem girdiniz.")

    if islem in ("+","-","*") or (islem == "/" and sayi2 != 0):
        print("Sonuc: ", sonuc)