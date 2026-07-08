# 📚 Kütüphane Yönetim Sistemi

Python ve SQLite kullanılarak geliştirilen, **Nesne Yönelimli Programlama (OOP)** prensiplerine uygun katmanlı mimariye sahip bir konsol tabanlı kütüphane yönetim sistemi.

## 🚀 Proje Hakkında

Bu proje, Python ile **OOP**, **SQLite** ve **katmanlı mimari** konularında pratik yapmak amacıyla geliştirilmiştir.

Uygulama üzerinden kitap ve kullanıcı işlemleri gerçekleştirilebilir. Ayrıca kitap ödünç alma sistemi için gerekli veritabanı altyapısı hazırlanmıştır.

---

## ✨ Özellikler

### 📖 Kitap İşlemleri

* Kitap ekleme
* Kitap silme
* Kitap arama
* Tüm kitapları listeleme

### 👤 Kullanıcı İşlemleri

* Kullanıcı ekleme
* Kullanıcı silme
* Kullanıcı arama
* Tüm kullanıcıları listeleme

### 📚 Ödünç Alma Sistemi

* Kitap ve kullanıcı arasında ilişki kurulması
* Foreign Key kullanımı
* Ödünç alma ve iade işlemleri için veritabanı altyapısı

---

## 🛠️ Kullanılan Teknolojiler

* Python
* SQLite
* Object-Oriented Programming (OOP)

---

## 🏛️ Proje Mimarisi

Proje, sorumlulukların birbirinden ayrıldığı katmanlı bir mimari ile geliştirilmiştir.

### Main

* Menülerin gösterilmesi
* Kullanıcıdan veri alınması
* İşlemlerin ilgili katmanlara yönlendirilmesi

### Operations

* İş kurallarının uygulanması
* Gerekli doğrulama işlemlerinin yapılması
* Database katmanı ile iletişim kurulması

### Database

* SQLite bağlantısının yönetilmesi
* SQL sorgularının çalıştırılması
* CRUD (Create, Read, Update, Delete) işlemlerinin gerçekleştirilmesi

---

## 🗄️ Veritabanı Yapısı

### Books

| Alan   | Açıklama                        |
| ------ | ------------------------------- |
| id     | Kitap ID (Otomatik oluşturulur) |
| name   | Kitap adı                       |
| author | Yazar                           |

### Users

| Alan | Açıklama                            |
| ---- | ----------------------------------- |
| id   | Kullanıcı ID (Otomatik oluşturulur) |
| name | Kullanıcı adı                       |

### Loans

| Alan    | Açıklama                    |
| ------- | --------------------------- |
| book_id | Ödünç alınan kitap          |
| user_id | Kitabı ödünç alan kullanıcı |

---

## 🎯 Bu Projede Kazandıklarım

Bu proje sayesinde aşağıdaki konularda pratik yapma fırsatı buldum:

* Nesne Yönelimli Programlama (OOP)
* Katmanlı mimari tasarımı
* SQLite ile veritabanı yönetimi
* CRUD işlemleri
* Exception yönetimi
* Modüler Python proje yapısı
* Foreign Key ilişkileri
* Katmanlar arası sorumluluk ayrımı

---

## 🚧 Geliştirilmesi Planlanan Özellikler

* Kitap güncelleme
* Kullanıcı güncelleme
* Ödünç alma ve iade işlemlerinin tamamlanması
* Teslim tarihi eklenmesi
* Geciken kitapların görüntülenmesi
* ISBN bilgisi
* Yayınevi bilgisi
* Yayın yılı
* Stok yönetimi

---

## 👨‍💻 Geliştirici

Bu proje, Python, SQLite ve Nesne Yönelimli Programlama konularında kendimi geliştirmek amacıyla hazırlanmıştır. Yeni özellikler eklenerek geliştirilmeye devam edilecektir.
