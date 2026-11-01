
print("HESAP MAKİNESİ")
print("----------------------------")

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

print("\nİŞLEM MENÜSÜ")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")
print("5. Üs alma (**)")
print("6. Tam bölme (//)")

islem = input("Yapmak istediğiniz işlemi giriniz: ")

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
        sonuc = sayi1 / sayi2
        print("Sonuç:", sonuc)
    else:
        print("Hata: Sıfıra bölme yapılamaz!")

elif islem == "**":
    sonuc = sayi1 ** sayi2
    print("Sonuç:", sonuc)

elif islem == "//":
    if sayi2 != 0:
        sonuc = sayi1 // sayi2
        print("Sonuç:", sonuc)
    else:
        print("Hata: Sıfıra bölme yapılamaz!")

else:
    print("Hatalı işlem seçtiniz!")
