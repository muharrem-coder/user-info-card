# ================================================
# GÜN 3 — MİNİ PROJE: Akıllı Görev Takip Sistemi (CLI)
# Konu: if/elif/else, while/for döngüsü, fonksiyonlar
# ================================================

# --- FONKSİYON TANIMLARI ---

def menu_goster():
    """Ana menüyü ekrana basar."""
    print("\n" + "=" * 38)
    print("     GÖREV TAKİP SİSTEMİ")
    print("=" * 38)
    print("  1 - Görev Ekle")
    print("  2 - Görevleri Listele")
    print("  3 - Görev Analizi")
    print("  4 - Görev Sil    (BOOST)")
    print("  5 - Çıkış")
    print("=" * 38)


def gorev_ekle(gorev_listesi):
    """
    Kullanıcıdan görev adı alır ve listeye ekler.
    Parametre: gorev_listesi (list)
    Return: Güncellenmiş liste
    """
    gorev_adi = input("  Görev adı girin : ").strip()
    if gorev_adi == "":
        print("  ⚠️  Boş görev eklenemez!")
        return gorev_listesi

    # Her görev sözlük olarak tutuluyor (BOOST: tamamlandı durumu)
    gorev = {"ad": gorev_adi, "tamamlandi": False}
    gorev_listesi.append(gorev)
    print(f"  ✅ '{gorev_adi}' eklendi.")
    return gorev_listesi


def gorev_listele(gorev_listesi):
    """
    Listedeki tüm görevleri numaralı şekilde yazdırır.
    Parametre: gorev_listesi (list)
    """
    if len(gorev_listesi) == 0:
        print("  📭 Henüz görev yok.")
        return

    print("\n  --- GÖREV LİSTESİ ---")
    # for döngüsü: listenin her elemanını sırayla işler
    for i, gorev in enumerate(gorev_listesi, start=1):
        durum = "✅" if gorev["tamamlandi"] else "⬜"
        print(f"  {i}. {durum} {gorev['ad']}")
    print("  " + "-" * 22)


def gorev_analizi(gorev_listesi):
    """
    Görev sayısına göre durum analizi yapar.
    if/elif/else kullanımı burada görülür.
    """
    sayi = len(gorev_listesi)
    tamamlanan = sum(1 for g in gorev_listesi if g["tamamlandi"])

    print("\n  --- GÖREV ANALİZİ ---")
    print(f"  Toplam Görev    : {sayi}")
    print(f"  Tamamlanan      : {tamamlanan}")

    # Koşullu ifade — if / elif / else
    if sayi == 0:
        print("  📌 Durum: Henüz görev eklenmemiş")
    elif sayi <= 3:
        print("  📌 Durum: Başlangıç seviyesi 🌱")
    else:
        print("  📌 Durum: Yoğun bir gün 🔥")


def gorev_sil(gorev_listesi):
    """
    BOOST: Kullanıcıdan numara alarak görev siler.
    """
    if len(gorev_listesi) == 0:
        print("  ⚠️  Silinecek görev yok.")
        return gorev_listesi

    gorev_listele(gorev_listesi)
    try:
        numara = int(input("  Silmek istediğiniz görev numarası: "))
        if 1 <= numara <= len(gorev_listesi):
            silinen = gorev_listesi.pop(numara - 1)
            print(f"  🗑️  '{silinen['ad']}' silindi.")
        else:
            print("  ⚠️  Geçersiz numara.")
    except ValueError:
        print("  ⚠️  Lütfen sayı girin.")
    return gorev_listesi


# --- ANA PROGRAM ---
def main():
    gorev_listesi = []  # Görevleri tutan liste

    # while döngüsü: kullanıcı çıkış yapmadan kapanmaz
    while True:
        menu_goster()
        secim = input("  Seçiminiz: ").strip()

        if secim == "1":
            gorev_listesi = gorev_ekle(gorev_listesi)

        elif secim == "2":
            gorev_listele(gorev_listesi)

        elif secim == "3":
            gorev_analizi(gorev_listesi)

        elif secim == "4":
            # BOOST: Görev silme
            gorev_listesi = gorev_sil(gorev_listesi)

        elif secim == "5":
            print("\n  👋 Görüşürüz! Görevlerin iyi gitsin.")
            break  # Döngüden çık

        else:
            print("  ⚠️  Geçersiz seçim. 1-5 arası girin.")


# Program buradan başlar
if __name__ == "__main__":
    main()

# ================================================
# ÖĞRENME NOTLARI:
#   - Fonksiyon: tekrar eden kodu bir kez yaz, çok kez kullan
#   - while: koşul doğru olduğu sürece döner
#   - for: listedeki her eleman için bir kez çalışır
#   - return: fonksiyondan değer döndürür
#   - if/elif/else: koşullara göre farklı yollar çalışır
#   -Gökce Hocam Merhaba ":)" hesabınızı takip ediyorum bi süredir içerikleriniz
#   gayet güzeller umarım bu şekilde devam edersiniz "<3"
# ================================================
