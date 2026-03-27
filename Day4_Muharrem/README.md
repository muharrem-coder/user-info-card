# 📘 Mini Proje: Dosya Tabanlı Görev Yöneticisi (OOP)

## 🧾 Proje Açıklaması
Bu proje, Python'da Nesne Yönelimli Programlama (OOP) ve dosya işlemlerini öğrenmek amacıyla geliştirilmiş bir görev yönetim sistemidir.

Görevler bir dosyaya kaydedilir ve program tekrar açıldığında kaldığı yerden devam eder.

---

## 🚀 Özellikler
- Görev ekleme
- Görevleri listeleme
- Görev silme
- Görev durumunu değiştirme (tamamlandı / bekliyor)
- Dosyaya kaydetme ve dosyadan yükleme

---

## 🧠 Kullanılan Yapılar

| Yapı | Açıklama |
|------|--------|
| `class` | OOP yapısı |
| `__init__` | Kurucu metot |
| `list` | Görev saklama |
| `dict` | Görev detayları |
| `file I/O` | Dosya okuma/yazma |
| `os` | Dosya kontrolü |

---

## 📌 Koddan Örnek

```python
gorev = {"ad": ad, "tamamlandi": False}
self.tasks.append(gorev)
```

---

## ▶️ Nasıl Çalıştırılır

1. Python yüklü olmalı
2. Terminalden çalıştır:

```bash
python dosya_adi.py
```

---

## 📁 Dosya Yapısı

Program çalıştığında:
- `tasks.txt` dosyası oluşturulur
- Görevler bu dosyada saklanır

Örnek kayıt:
```
Alışveriş yap|False
Python çalış|True
```

---

## 📊 Menü Sistemi

```
1 - Görev Ekle
2 - Görevleri Listele
3 - Görev Sil
4 - Tamamlandı İşaretle
5 - Kaydet ve Çık
```

---

## 📚 Öğrenme Notları

- OOP, büyük projelerde düzen sağlar
- `self` nesneye erişimi temsil eder
- `open()` ile dosya işlemleri yapılır
- `with open()` dosya güvenliğini sağlar
- Veri kalıcılığı (persistence) bu projede uygulanır

---

## 👨‍💻 Amaç
Bu proje, Python'da gerçek dünya senaryolarına daha yakın bir sistem geliştirerek OOP ve dosya yönetimini öğretmeyi hedefler.
