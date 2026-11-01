print("HESAP MAKİNESİ")

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

islem = input("İşlemi giriniz (+, -, *, /, **, //): ")

if islem == "+":
    sonuc = sayi1 + sayi2
    print("Sonuç:", sonuc)

elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Sonuç:", sonuc)

elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Sonuç:", sonuc)

elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

elif islem == "//":
    if sayi2 != 0:
        print("Sonuç:", sayi1 // sayi2)
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

elif islem == "**":
    print("Sonuç:", sayi1 ** sayi2)

else:
    print("Geçersiz işlem.")
