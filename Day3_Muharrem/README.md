# 📘 Mini Proje: Akıllı Görev Takip Sistemi (CLI)

## 🧾 Proje Açıklaması
Bu proje, Python'da fonksiyonlar, döngüler ve koşul yapıları kullanılarak geliştirilmiş komut satırı (CLI) tabanlı bir görev takip sistemidir.

Kullanıcı; görev ekleyebilir, listeleyebilir, analiz edebilir ve silebilir. Sistem tamamen terminal üzerinden çalışır.

---

## 🚀 Özellikler
- Görev ekleme
- Görevleri listeleme
- Görev analizi (toplam & tamamlanan)
- Görev silme
- Sonsuz döngü ile menü sistemi (CLI)

---

## 🧠 Kullanılan Yapılar

| Yapı | Açıklama |
|------|--------|
| `function` | Kod tekrarını önler |
| `while` | Menü döngüsü |
| `for` | Liste işlemleri |
| `if/elif/else` | Karar mekanizması |
| `list` | Görev saklama |
| `dict` | Görev detayları |

---

## 📌 Koddan Örnek

```python
gorev = {"ad": gorev_adi, "tamamlandi": False}
gorev_listesi.append(gorev)
```

---

## ▶️ Nasıl Çalıştırılır

1. Python kurulu olmalı
2. Terminalden çalıştır:

```bash
python dosya_adi.py
```

---

## 📊 Örnek Kullanım

```
======================================
     GÖREV TAKİP SİSTEMİ
======================================
1 - Görev Ekle
2 - Görevleri Listele
3 - Görev Analizi
4 - Görev Sil
5 - Çıkış
======================================
```

---

## 📈 Analiz Özelliği

Sistem aşağıdaki bilgileri sunar:
- Toplam görev sayısı
- Tamamlanan görev sayısı
- Durum değerlendirmesi (başlangıç / yoğunluk)

---

## 📚 Öğrenme Notları

- Fonksiyonlar modüler programlama sağlar
- `while True` sürekli çalışan sistemler için kullanılır
- `enumerate()` index ile listeyi dolaşmayı sağlar
- `dict` veri yapısı anahtar-değer mantığıyla çalışır
- `try/except` hata kontrolü sağlar

---

## 👨‍💻 Amaç
Bu proje, Python'da daha kompleks yapıların (fonksiyonlar + döngüler + veri yapıları) birlikte nasıl çalıştığını öğretmeyi hedefler.
