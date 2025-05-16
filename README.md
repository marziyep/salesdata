# salesdata
Günlük Ürün Satış Performans Analizi (2024 - Q1)
Veri seti, 1 Ocak 2024 - 30 Nisan 2024 tarihleri arasında 5 farklı ürünün günlük satış bilgilerini içermektedir:

    Tarih: Satışın gerçekleştiği tarih

    Ürün: Satılan ürünün adı (Ürün A - E)

    Birim Fiyat: Ürünün o günkü birim fiyatı (TL)

    Satış Adedi: O gün satılan toplam adet

    Toplam Satış: Birim fiyat × satış adedi

Toplam veri sayısı: 610 kayıt (122 gün × 5 ürün)


Amaç:

Bu projede, 5 farklı ürünün 2024 yılı ilk çeyreğindeki (Ocak-Nisan) satış performansı analiz edilmiştir. Amaç, ürün bazında satış eğilimlerini, genel satış hacmini, fiyat ve satış adedi ilişkilerini belirlemek ve karar destek sistemlerine içgörü sağlamaktır.
Veri Seti Açıklaması:

Veri seti simüle edilmiş olup, bir perakende şirketinin 5 ürününe ait günlük satış verilerini içermektedir. 122 gün boyunca her ürün için:

    Günlük satış adedi (Poisson dağılımı ile üretilmiştir)

    Günlük fiyat (uniform dağılım)

    Toplam günlük satış

Analiz Adımları:

    Veri Temizliği & İstatistiksel İnceleme: Aykırı değer kontrolü ve dağılımlar

    Zaman Serisi Analizi: Günlük toplam satışlar ve ürün bazında satış trendleri

    Ürün Kıyaslaması: Hangi ürünün daha fazla gelir ürettiği

    Korelasyon Analizi: Fiyat, satış adedi ve toplam satış arasındaki ilişki

    Performans Zirvesi: En yüksek gelirin elde edildiği gün

Bulgular:

    En çok gelir getiren ürün: Ürün B

    En yoğun satış günü: {en_iyi_gun.date()}, toplam {en_yuksek_satis:.2f} TL

    Birim fiyat ve satış adedi arasında negatif korelasyon gözlenmiştir (yani fiyat arttıkça satış miktarı düşme eğiliminde).

    Satış adetleri genelde 15-25 aralığında yoğunlaşmıştır.

Öneriler:

    Fiyat optimizasyonu yapılabilir: Ürünlerin satış adetleriyle fiyat ilişkisi modellendirilerek maksimum gelir stratejileri geliştirilebilir.

    Ürün B’ye yatırım artırılabilir, reklam kampanyaları yoğunlaştırılabilir.

    Zayıf performanslı ürünler (örneğin Ürün E), ürün portföyü içinde yeniden değerlendirilmelidir.
