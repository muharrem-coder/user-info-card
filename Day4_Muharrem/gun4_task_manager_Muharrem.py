# ================================================
# GÜN 4 — MİNİ PROJE: Dosya Tabanlı Görev Yöneticisi (OOP)
# Konu: Sınıflar (class), Dosya Yönetimi (open/read/write)
# ================================================

import os


class TaskManager:
    """
    Görevleri dosyaya kaydeden ve okuyan yönetici sınıfı.
    
    Attributes:
        self.tasks    : Görevleri tutan liste
        self.filename : Kayıt dosyasının adı
    
    OOP neden gerekli?
        → Görev listesi + dosya adı + tüm işlemler
          tek bir nesne altında toplanır.
          Her şey bir arada, düzenli ve genişletilebilir.
    """

    def __init__(self, filename="tasks.txt"):
        """
        Kurucu metot: nesne oluşturulunca otomatik çalışır.
        Dosya varsa görevleri yükler.
        """
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # ---- DOSYADAN OKU ----
    def load_tasks(self):
        """
        Dosya mevcutsa içindeki görevleri listeye yükler.
        Dosya yoksa sessizce devam eder.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                satirlar = f.readlines()
                for satir in satirlar:
                    satir = satir.strip()
                    if "|" in satir:
                        parcalar = satir.split("|")
                        ad = parcalar[0]
                        # BOOST: tamamlandı durumunu da oku
                        tamamlandi = parcalar[1] == "True"
                        self.tasks.append({"ad": ad, "tamamlandi": tamamlandi})
            print(f"  ✅ {len(self.tasks)} kayıtlı görev yüklendi.")
        else:
            print("  📄 Yeni görev dosyası oluşturulacak.")

    # ---- DOSYAYA YAZ ----
    def save_tasks(self):
        """
        Listedeki tüm görevleri dosyaya kaydeder.
        "w" modu: dosyayı sıfırdan yazar (üzerine yazar).
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            for gorev in self.tasks:
                # Format: "görev adı|True" ya da "görev adı|False"
                f.write(f"{gorev['ad']}|{gorev['tamamlandi']}\n")
        print(f"  💾 {len(self.tasks)} görev '{self.filename}' dosyasına kaydedildi.")

    # ---- GÖREV EKLE ----
    def add_task(self):
        """Kullanıcıdan görev alır ve listeye ekler."""
        ad = input("  Görev adı: ").strip()
        if ad == "":
            print("  ⚠️  Boş görev eklenemez.")
            return
        self.tasks.append({"ad": ad, "tamamlandi": False})
        print(f"  ✅ '{ad}' eklendi.")

    # ---- GÖREVLERİ LİSTELE ----
    def list_tasks(self):
        """Tüm görevleri numaralı olarak yazdırır."""
        if not self.tasks:
            print("  📭 Görev listesi boş.")
            return
        print("\n  --- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(self.tasks, 1):
            durum = "✅" if gorev["tamamlandi"] else "⬜"
            print(f"  {i}. {durum} {gorev['ad']}")
        print("  " + "-" * 22)

    # ---- BOOST: GÖREV SİL ----
    def delete_task(self):
        """Belirtilen numaralı görevi siler."""
        self.list_tasks()
        if not self.tasks:
            return
        try:
            numara = int(input("  Silinecek görev numarası: "))
            if 1 <= numara <= len(self.tasks):
                silinen = self.tasks.pop(numara - 1)
                print(f"  🗑️  '{silinen['ad']}' silindi.")
            else:
                print("  ⚠️  Geçersiz numara.")
        except ValueError:
            print("  ⚠️  Sayı giriniz.")

    # ---- BOOST: TAMAMLANDI İŞARETLE ----
    def toggle_task(self):
        """Görevi tamamlandı / tamamlanmadı olarak değiştirir."""
        self.list_tasks()
        if not self.tasks:
            return
        try:
            numara = int(input("  Durumu değiştirilecek görev numarası: "))
            if 1 <= numara <= len(self.tasks):
                gorev = self.tasks[numara - 1]
                gorev["tamamlandi"] = not gorev["tamamlandi"]
                yeni_durum = "✅ Tamamlandı" if gorev["tamamlandi"] else "⬜ Bekliyor"
                print(f"  '{gorev['ad']}' → {yeni_durum}")
            else:
                print("  ⚠️  Geçersiz numara.")
        except ValueError:
            print("  ⚠️  Sayı giriniz.")

            #I HAVE MY EYES ON YOU ":)"
# ---- ANA PROGRAM ----
def main():
    print("=" * 40)
    print("  DOSYA TABANLI GÖREV YÖNETİCİSİ")
    print("=" * 40)

    # Nesne oluştur → __init__ çalışır → dosya varsa yükler
    manager = TaskManager(filename="tasks.txt")

    while True:
        print("\n  --- MENÜ ---")
        print("  1 - Görev Ekle")
        print("  2 - Görevleri Listele")
        print("  3 - Görev Sil        (BOOST)")
        print("  4 - Tamamlandı İşaretle (BOOST)")
        print("  5 - Kaydet ve Çık")
        print("  " + "-" * 22)

        secim = input("  Seçim: ").strip()

        if secim == "1":
            manager.add_task()
        elif secim == "2":
            manager.list_tasks()
        elif secim == "3":
            manager.delete_task()
        elif secim == "4":
            manager.toggle_task()
        elif secim == "5":
            manager.save_tasks()
            print("  👋 Görevler kaydedildi. Çıkılıyor...")
            break
        else:
            print("  ⚠️  Geçersiz seçim.")


if __name__ == "__main__":
    main()

# ================================================
# ÖĞRENME NOTLARI:
#   - class: birbiriyle ilişkili veri + fonksiyonları bir araya getirir
#   - __init__: nesne oluşturulunca ilk çalışan metot
#   - self: nesnenin kendisini temsil eder
#   - open("r"): okuma, open("w"): yazma, open("a"): ekleme
#   - OOP neden gerekli? → Büyüyen projelerde düzen + yeniden kullanım
#   -YOU SHOULD NOT SEE THIS nah just kidding ":)"
# ================================================
