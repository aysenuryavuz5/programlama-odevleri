
print("HESAP MAKINESI")

sayi1 = float(input("Birinci sayiyi gir: "))
sayi2 = float(input("Ikinci sayiyi gir: "))

print("Toplama:", sayi1 + sayi2)
print("Cikarma:", sayi1 - sayi2)
print("Carpma:", sayi1 * sayi2)

if sayi2 != 0:
    print("Bolme:", sayi1 / sayi2)
    print("Tam bolme:", sayi1 // sayi2)
else:
    print("Sifira bolme yapilamaz!")

print("Us alma:", sayi1 ** sayi2)