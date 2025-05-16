import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
df = pd.read_csv("satis_verisi.csv", parse_dates=["Tarih"])

# Özet istatistikler
print("Genel İstatistikler:\n", df.describe())

# Ürün bazında toplam satış
urun_toplam = df.groupby("Ürün")["Toplam Satış"].sum().sort_values(ascending=False)
print("\nÜrün Bazında Toplam Satış:\n", urun_toplam)

# Zaman serisinde toplam satış
gunluk_toplam = df.groupby("Tarih")["Toplam Satış"].sum()

plt.figure(figsize=(14, 5))
sns.lineplot(x=gunluk_toplam.index, y=gunluk_toplam.values)
plt.title("Günlük Toplam Satışlar (Tüm Ürünler)")
plt.xlabel("Tarih")
plt.ylabel("TL")
plt.grid(True)
plt.tight_layout()
plt.show()

# Ürün bazında ortalama satış trendi
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x="Tarih", y="Toplam Satış", hue="Ürün")
plt.title("Ürün Bazında Günlük Satış Trendleri")
plt.xlabel("Tarih")
plt.ylabel("Toplam Satış (TL)")
plt.legend(title="Ürün")
plt.grid(True)
plt.tight_layout()
plt.show()

# Korelasyon analizi
corr = df[["Birim Fiyat", "Satış Adedi", "Toplam Satış"]].corr()
print("\nKorelasyon Matrisi:\n", corr)

sns.heatmap(corr, annot=True, cmap="viridis")
plt.title("Korelasyon Matrisi")
plt.show()

# En iyi gün analizi
en_iyi_gun = gunluk_toplam.idxmax()
en_yuksek_satis = gunluk_toplam.max()
print(f"\nEn yüksek satış yapılan gün: {en_iyi_gun.date()} - {en_yuksek_satis:.2f} TL")
