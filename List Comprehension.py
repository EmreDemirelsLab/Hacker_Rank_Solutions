if __name__ == '__main__':
    x = int(input('1:'))
    y = int(input('2:'))
    z = int(input('3:'))
    n = int(input('n:'))
    result = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]
    print(result)


# list comprehensions (liste kapsamlılıkları) ile ilgili öğrenme sürecinde oldukça faydalı olacak bir örnek üzerinden gidiyoruz.
# Bu soruda, 3D bir ızgarada verilen boyutlarda (a, b, c) ve bir tamsayı (n) olan bir küp üzerinde belirli koşullara göre
# koordinatları üretip yazdırmamız isteniyor.
#
# Görev
# Verilen dört tamsayıyı kullanarak:
#
# Boyutlar: a, b, c (bunlar, küpün boyutları),
#
# Koşul: Koordinatların toplamı n'ye eşit olmamalıdır.
#
# Aşağıda, örneği açıklayarak çözümün nasıl yapılacağını adım adım ele alalım:
#
# Girdi:
# İlk satırda a (x boyutu),
#
# İkinci satırda b (y boyutu),
#
# Üçüncü satırda c (z boyutu),
#
# Dördüncü satırda ise n (koşul).
#
# Bu dört sayı verildiğinde, a, b ve c boyutlarında her bir koordinat çiftinin toplamını kontrol etmemiz gerekiyor ve toplamı n olanları çıkarıyoruz.
#
# Çözüm Adımları:
# List comprehension kullanarak her bir x, y, z kombinasyonunu oluşturacağız. Bu üçlü kombinasyonları şöyle düşünebiliriz:
#
# x 0'dan a-1'e kadar,
#
# y 0'dan b-1'e kadar,
#
# z 0'dan c-1'e kadar.
#
# Ardından, bu üçlülerin x + y + z != n koşuluna uyanlarını seçip listeleyeceğiz.
#
# Sonuç olarak, n'ye eşit olmayan toplamlar içeren koordinatların listesini döndüreceğiz.

