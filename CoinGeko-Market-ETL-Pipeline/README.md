# CoinGecko Crypto Market ETL Pipeline

Bu proje, CoinGecko API'sinden kripto para piyasası verilerini çekerek **ETL (Extract, Transform, Load)** sürecini gerçekleştiren basit bir veri mühendisliği projesidir. Çekilen veriler temizlenir, yeni metrikler oluşturulur ve SQLite veritabanına kaydedilir.

## 🚀 Kullanılan Teknolojiler

* Python
* Pandas
* SQLite
* Requests
* Logging

## 📁 Proje Yapısı

```text
CoinGecko Crypto Market ETL Pipeline/
│
├── Extract/
├── Transform/
├── Load/
├── Logs/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## 🔄 ETL Süreci

### Extract

* CoinGecko API'sinden güncel kripto para verileri çekilir.
* Toplam kripto para piyasa değeri alınır.

### Transform

* Gereksiz sütunlar kaldırılır.
* Eksik veriler temizlenir.
* Yeni özellikler oluşturulur:

  * Market Dominance
  * Market Cap Category
  * Price Change Direction
  * Dilution Risk
  * Circulation Ratio
  * Daily Price Range

### Load

* Gerekli tablolar oluşturulur.
* Yeni coinler **Coin** tablosuna eklenir.
* Mevcut coin bilgileri güncellenir.
* Günlük piyasa verileri **MarketHistory** tablosuna kaydedilir.

## 🗄️ Veritabanı

Projede iki tablo kullanılmaktadır.

### Coin

Her kripto paranın güncel bilgilerini saklar.

### MarketHistory

Kripto paraların zamana bağlı piyasa geçmişini saklar.

## 📝 Loglama

ETL süreci boyunca aşağıdaki işlemler log dosyasına kaydedilir:

* ETL başlangıcı ve bitişi
* API istekleri
* Veri dönüştürme işlemleri
* Veritabanı işlemleri
* Oluşan hata ve istisnalar

## 📊 Veri Kaynağı

* CoinGecko API

## 📌 Gelecekte Eklenmesi Planlanan Özellikler

* PostgreSQL desteği
* Docker desteği
* Otomatik zamanlanmış ETL (Scheduler)
* Streamlit ile dashboard
* Unit testler
* Veri görselleştirme

