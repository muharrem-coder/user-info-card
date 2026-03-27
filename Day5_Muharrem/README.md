# 🧮 Modular Safe Calculator (Python)

> **Modüler yapı, hata yönetimi ve temiz kod prensipleriyle geliştirilmiş CLI tabanlı hesap makinesi**

---

## 📌 Proje Hakkında

Bu proje, Python’da:

- Modüler programlama (modular design)
- Hata yönetimi (exception handling)
- Kullanıcı girdisi doğrulama (input validation)
- Loglama (logging)

konularını pratik olarak göstermek amacıyla geliştirilmiş bir komut satırı (CLI) uygulamasıdır.

---

## 🏗️ Mimari Tasarım

```
.
├── main.py
├── operations.py
├── utils.py
└── errors.log
```

---

## ⚙️ Özellikler

- Güvenli kullanıcı input sistemi
- Gelişmiş hata yakalama
- Sıfıra bölme koruması
- Log dosyasına hata kaydı
- Modüler yapı
- CLI menü sistemi

---

## 🔢 Desteklenen İşlemler

- Toplama
- Çıkarma
- Çarpma
- Bölme
- Üs alma
- Mod alma

---

## 🚀 Kurulum & Çalıştırma

```
python main.py
```

---

## 🖥️ Kullanım

Program çalıştığında kullanıcıdan işlem seçmesi ve iki sayı girmesi istenir. Sonuç ekrana yazdırılır.

---

## 🧠 Hata Yönetimi

- ValueError → yanlış input
- ZeroDivisionError → sıfıra bölme
- Exception → genel hatalar

Tüm hatalar log dosyasına yazılır.

---

## 📝 Loglama

Hatalar `errors.log` dosyasına kaydedilir.

---

## 📐 Tasarım Prensipleri

- Separation of Concerns
- Single Responsibility Principle
- Defensive Programming

---

## 🔧 Geliştirme Önerileri

- logging modülü entegrasyonu
- GUI versiyon
- unit testler
- type hints

---

## 🎯 Amaç

Python’da modüler yapı ve hata yönetimini öğretmek.
