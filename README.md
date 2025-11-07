# Salary Insights – Experience & Education Analysis  
*İş Deneyimi, Eğitim ve Maaş Analizi Projesi / Job Experience, Education & Salary Analysis Project*

---

## Proje Hakkında | About the Project

Bu proje, çalışanların yaş, cinsiyet, eğitim seviyesi, iş unvanı ve deneyim yılına göre maaş ilişkilerini analiz etmek için hazırlanmıştır.  
Python veri analizi kütüphaneleri (Pandas, NumPy, Seaborn, Matplotlib) kullanılmıştır.  
Amaç, maaşı etkileyen temel faktörleri belirlemek ve görselleştirmelerle desteklenmiş içgörüler üretmektir.

This project aims to analyze salary patterns based on employee **age, gender, education level, job title**, and **years of experience**.  
It uses Python data analysis libraries (Pandas, NumPy, Seaborn, Matplotlib) to identify salary trends and create visual insights.

---

##  Kullanılan Teknolojiler | Technologies Used

- **Python 3**
- **Pandas** – Data cleaning & preprocessing  
- **NumPy** – Statistical operations & correlation  
- **Seaborn** – High-level data visualization  
- **Matplotlib** – Graph customization and saving plots  

---

##  Veri Seti | Dataset

Dosya: `Salary_Data.csv`

| Column Name | Açıklama (Türkçe) | Description (English) |
|--------------|------------------|------------------------|
| Age | Çalışanın yaşı | Employee age |
| Gender | Cinsiyet | Gender |
| Education Level | Eğitim düzeyi | Level of education |
| Job Title | İş unvanı | Job title |
| Years of Experience | Deneyim yılı | Years of experience |
| Salary | Maaş (USD) | Salary (USD) |

---

##  Analiz Adımları | Analysis Steps

1. **Veri Temizleme (Data Cleaning)**  
   - Eksik veriler kaldırıldı (`dropna`)  
   - Sayısal veriler için tür dönüşümü yapıldı (`astype`)  

2. **İstatistiksel Analiz (Statistical Overview)**  
   - Ortalama, medyan, minimum ve maksimum maaş hesaplandı  
   - Deneyim, yaş ve maaş arasındaki korelasyon analiz edildi  

3. **Görselleştirme (Visualization)**  
   - Maaş dağılımı (Histogram)  
   - Deneyim-Maaş ilişkisi (Scatterplot)  
   - Cinsiyete göre maaş farkı (Boxplot)  
   - Eğitim düzeyine göre ortalama maaş (Bar chart)  
   - En yüksek maaşlı meslekler (Top 10 bar chart)  
   - Yaş-Maaş ilişkisi (Regression plot)  
   - Korelasyon matrisi (Heatmap)  

---

## Örnek Grafikler | Sample Visuals

Tüm grafikler `outputs/figures/` klasörüne kaydedilir.

-  `salary_distribution.png` – Maaş dağılımı  
-  `experience_salary.png` – Deneyim & maaş ilişkisi  
-  `gender_salary.png` – Cinsiyete göre maaş farkı  
-  `education_salary.png` – Eğitim düzeyine göre maaş ortalaması  
-  `top_jobs.png` – En yüksek maaşlı 10 meslek  
-  `age_salary.png` – Yaş ve maaş ilişkisi  
-  `correlation_matrix.png` – Korelasyon matrisi  

---

##  Çıktı & İçgörüler | Key Insights

- Ortalama maaş deneyimle birlikte artmaktadır.  
- Eğitim düzeyi yüksek olanlar daha yüksek maaş almaktadır.  
- Cinsiyet bazında küçük maaş farklılıkları gözlemlenmiştir.  
- En yüksek ortalama maaş genellikle **Senior Data Scientist** gibi teknik pozisyonlardadır.

---

##  Proje Dosyaları | Project Structure

Salary Insights – Experience & Education Analysis/
│
├── kod.py
├── Salary_Data.csv
├── outputs/
│ └── figures/
│ ├── salary_distribution.png
│ ├── experience_salary.png
│ ├── gender_salary.png
│ ├── education_salary.png
│ ├── top_jobs.png
│ ├── age_salary.png
│ └── correlation_matrix.png
