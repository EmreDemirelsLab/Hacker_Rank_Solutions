if __name__ == '__main__':
    n = int(input())  # Bu değeri aslında kullanmıyoruz
    arr = map(int, input().split())  # Kullanıcıdan alınan puanları integer listesine dönüştürüyoruz

    arr = list(arr)  # map object'ini listeye dönüştürmek gerekiyor

    # Küme oluşturuyoruz, böylece tekrarlanan puanlar silinir
    unique_scores = set(arr)

    # En yüksek puanı çıkarıyoruz
    unique_scores.remove(max(unique_scores))

    # Geriye kalan en yüksek puan, runner-up olacaktır
    print(max(unique_scores))


Bu soruda, verilen bir puanlar listesinde runner-up yani ikinci en yüksek puanı bulmamız gerekiyor.
Runner-up, en yüksek puandan sonra gelen en büyük puandır.

Adım adım çözüm:
Verilen Girdi:

İlk satırda, n adlı bir tam sayı var. Bu, oyuncu sayısını belirtir. Ancak bu değeri kullanmamıza gerek yok,
çünkü ikinci satırdaki listeyi doğrudan alabiliriz.

İkinci satırda, n oyuncunun puanları bir liste olarak verilmiştir. Bu puanlar arasında aynı puanlar olabilir.

Çözüm Planı:

İlk olarak, verilen listeyi alıyoruz.

Daha sonra, bu listeyi set (küme) yapısına dönüştürüyoruz. Çünkü küme, tekrarlanan değerleri otomatik olarak siler.

Küme içindeki en büyük iki değeri buluyoruz. İlk olarak max() fonksiyonu ile en yüksek puanı, sonra bu maksimum puanı
kümeden çıkararak ikinci en yüksek puanı buluyoruz.

