import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


# AYARLAR VE KLASÖR OLUŞTURMA

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False
sns.set(style="whitegrid")

output_dir = "outputs/figures"
os.makedirs(output_dir, exist_ok=True)


# VERİYİ YÜKLE VE GENEL BAKIŞ

df = pd.read_csv("Salary_Data.csv")

print("=== Veri İlk 5 Satır ===")
print(df.head(), "\n")

print("=== Veri Bilgisi ===")
print(df.info(), "\n")

print("=== Eksik Değerler ===")
print(df.isnull().sum(), "\n")

# Eksik değer varsa temizle
df.dropna(inplace=True)


# TEMEL İSTATİSTİKSEL ANALİZ

print("=== Sayısal Özet ===")
print(df.describe(), "\n")

print("Toplam Gözlem Sayısı:", len(df))
print("Toplam Meslek Sayısı:", df["Job Title"].nunique())
print("Toplam Eğitim Düzeyi:", df["Education Level"].nunique(), "\n")

mean_salary = df["Salary"].mean()
median_salary = df["Salary"].median()

print(f"Ortalama Maaş: ${mean_salary:,.0f}")
print(f"Medyan Maaş: ${median_salary:,.0f}\n")


# GÖRSEL ANALİZLER


# Maaş Dağılımı
plt.figure(figsize=(9,5))
sns.histplot(df["Salary"], bins=30, kde=True, color="skyblue")
plt.title("Maaş Dağılımı")
plt.xlabel("Maaş ($)")
plt.ylabel("Frekans")
plt.tight_layout()
plt.savefig(f"{output_dir}/maas_dagilimi.png", dpi=300)
plt.show()

#  Deneyim ve Maaş İlişkisi
plt.figure(figsize=(8,6))
sns.scatterplot(x="Years of Experience", y="Salary", data=df, hue="Education Level", palette="cool")
plt.title("Deneyim ve Maaş İlişkisi (Eğitim Düzeyine Göre)")
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş ($)")
plt.legend(title="Eğitim Düzeyi")
plt.tight_layout()
plt.savefig(f"{output_dir}/deneyim_maas_iliskisi.png", dpi=300)
plt.show()

#  Cinsiyete Göre Maaş
plt.figure(figsize=(7,5))
sns.boxplot(x="Gender", y="Salary", data=df, palette="pastel")
plt.title("Cinsiyete Göre Maaş Dağılımı")
plt.xlabel("Cinsiyet")
plt.ylabel("Maaş ($)")
plt.tight_layout()
plt.savefig(f"{output_dir}/cinsiyet_maas.png", dpi=300)
plt.show()

#  Eğitim Düzeyine Göre Ortalama Maaş
plt.figure(figsize=(9,5))
edu_salary = df.groupby("Education Level")["Salary"].mean().sort_values(ascending=False)
sns.barplot(x=edu_salary.index, y=edu_salary.values, palette="Blues_r")
plt.title("Eğitim Düzeyine Göre Ortalama Maaş")
plt.xlabel("Eğitim Düzeyi")
plt.ylabel("Ortalama Maaş ($)")
plt.tight_layout()
plt.savefig(f"{output_dir}/egitim_maas.png", dpi=300)
plt.show()

#  En Yüksek Maaşlı 10 Meslek
plt.figure(figsize=(10,6))
top_jobs = df.groupby("Job Title")["Salary"].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="Greens_r")
plt.title("En Yüksek Ortalama Maaşa Sahip 10 Meslek")
plt.xlabel("Ortalama Maaş ($)")
plt.ylabel("Meslek")
plt.tight_layout()
plt.savefig(f"{output_dir}/top10_meslek.png", dpi=300)
plt.show()

#  Yaş ile Maaş Arasındaki İlişki
plt.figure(figsize=(8,6))
sns.regplot(x="Age", y="Salary", data=df, color="coral")
plt.title("Yaş ve Maaş Arasındaki İlişki")
plt.xlabel("Yaş")
plt.ylabel("Maaş ($)")
plt.tight_layout()
plt.savefig(f"{output_dir}/yas_maas_iliskisi.png", dpi=300)
plt.show()


# KORELASYON ANALİZİ

num_cols = ["Age", "Years of Experience", "Salary"]
corr = df[num_cols].corr()

print("=== Sayısal Değişkenler Arasındaki Korelasyon ===")
print(corr, "\n")

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.tight_layout()
plt.savefig(f"{output_dir}/korelasyon_matrisi.png", dpi=300)
plt.show()


# İÇGÖRÜLER

print("=== Analiz Sonuçları ===")
print(f"- Ortalama maaş: ${mean_salary:,.0f}, medyan maaş: ${median_salary:,.0f}.")
print("- Maaşlar deneyim ile pozitif yönde ilişkili (korelasyon: "
      f"{round(corr.loc['Years of Experience','Salary'],2)}).")
print("- En yüksek ortalama maaş eğitim düzeyi:", edu_salary.index[0])
print("- En yüksek maaş ortalamasına sahip meslek:", top_jobs.index[0])
