# 1. Kullanıcıdan iki sayı alınır (ondalıklı olabileceği icin float kullanılmıstır)
birinci_sayi = float(input("Birinci sayıyı giriniz: "))
ikinci_sayi = float(input("İkinci sayıyı giriniz: "))

# 2. Kullanıcıdan islem operatoru alınır
islem = input("İslemi giriniz (+, -, *, /, **, //): ")

# 3, 4, 5 ve 6. Kosul ifadeleriyle islemlerin gerceklestirilmesi ve kontrolu
if islem == "+":
    sonuc = birinci_sayi + ikinci_sayi
    print(f"Sonuc: {sonuc}")

elif islem == "-":
    sonuc = birinci_sayi - ikinci_sayi
    print(f"Sonuc: {sonuc}")

elif islem == "*":
    sonuc = birinci_sayi * ikinci_sayi
    print(f"Sonuc: {sonuc}")

elif islem == "/":
    # Sıfıra bölme hatası kontrolü
    if ikinci_sayi == 0:
        print("Hata: Bir sayı sıfıra bolunemez.")
    else:
        sonuc = birinci_sayi / ikinci_sayi
        print(f"Sonuc: {sonuc}")

elif islem == "**":
    sonuc = birinci_sayi ** ikinci_sayi
    print(f"Sonuc: {sonuc}")

elif islem == "//":
    # Sıfıra bölme hatası kontrolü
    if ikinci_sayi == 0:
        print("Hata: Bir sayı sıfıra bolunemez.")
    else:
        sonuc = birinci_sayi // ikinci_sayi
        print(f"Sonuc: {sonuc}")

else:
    # Listelenmeyen bir operator girildiğinde calısan kısım
    print("Gecersiz islem.")

