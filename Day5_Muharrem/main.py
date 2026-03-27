# ================================================
# main.py — Ana Program
# GÜN 5 — MİNİ PROJE: Modüler Güvenli Hesap Makinesi
# Konu: try/except/else/finally, import, modüller
# ================================================

# Kendi modüllerimizi import ediyoruz
from operations import topla, cikar, carp, bol, us_al, mod_al
from utils import guvenli_sayi_al, hata_logla, baslik_yazdir


def menu_goster():
    """İşlem menüsünü ekrana basar."""
    print("\n  --- İŞLEM SEÇ ---")
    print("  1 - Toplama   (+)")
    print("  2 - Çıkarma   (-)")
    print("  3 - Çarpma    (×)")
    print("  4 - Bölme     (÷)")
    print("  5 - Üs Alma   (^)  [BOOST]")
    print("  6 - Mod Alma  (%)  [BOOST]")
    print("  7 - Çıkış")
    print("  " + "-" * 22)


def islemi_calistir(secim, a, b):
    """
    Seçilen işlemi çalıştırır.
    try/except ile hata yönetimi burada yapılır.
    
    try   : Tehlikeli kodu dene
    except: Hata oluşursa yakala
    else  : Hata yoksa çalış
    finally: Her durumda çalış
    """
    islem_adi = {
        "1": "Toplama", "2": "Çıkarma", "3": "Çarpma",
        "4": "Bölme",   "5": "Üs Alma", "6": "Mod Alma"
    }.get(secim, "Bilinmiyor")

    try:
        if secim == "1":
            sonuc = topla(a, b)
        elif secim == "2":
            sonuc = cikar(a, b)
        elif secim == "3":
            sonuc = carp(a, b)
        elif secim == "4":
            sonuc = bol(a, b)       # ZeroDivisionError olabilir
        elif secim == "5":
            sonuc = us_al(a, b)
        elif secim == "6":
            sonuc = mod_al(a, b)    # ZeroDivisionError olabilir
        else:
            print("  ⚠️  Geçersiz seçim.")
            return

    except ZeroDivisionError as hata:
        # Sıfıra bölme hatası yakalandı
        print(f"  ❌ HATA: {hata}")
        hata_logla(islem_adi, str(hata))   # BOOST: log'a yaz
        return

    except Exception as hata:
        # Beklenmeyen diğer hatalar
        print(f"  ❌ Beklenmeyen hata: {hata}")
        hata_logla(islem_adi, str(hata))
        return

    else:
        # Hata yoksa sonucu göster
        print(f"\n  ✅ Sonuç: {a} {islem_adi} {b} = {sonuc}")

    finally:
        # Her durumda bu blok çalışır
        print(f"  (İşlem tamamlandı: {islem_adi})")


# ---- ANA PROGRAM ----
def main():
    baslik_yazdir("MODÜLER GÜVENLİ HESAP MAKİNESİ")
    print("  Modüller: operations.py, utils.py")

    while True:
        menu_goster()
        secim = input("  Seçiminiz: ").strip()

        if secim == "7":
            print("\n  👋 Hesap makinesi kapatıldı.")
            break

        if secim not in ["1", "2", "3", "4", "5", "6"]:
            print("  ⚠️  Geçersiz seçim. 1-7 arası girin.")
            continue

        # utils.py'den güvenli input al
        a = guvenli_sayi_al("1. sayı")
        b = guvenli_sayi_al("2. sayı")

        islemi_calistir(secim, a, b)


if __name__ == "__main__":
    main()

# ================================================
# ÖĞRENME NOTLARI:
#   - import: başka dosyadaki fonksiyonları çağırır
#   - try   : hata çıkabilecek kodu dene
#   - except: belirli hatayı yakala
#   - else  : try başarılıysa çalış
#   - finally: her koşulda çalış (temizlik için ideal)
#   - Modül kullanmanın avantajı:
#       → Her dosyanın tek bir sorumluluğu var
#       → Kod okunur, test edilir, yeniden kullanılabilir
# ================================================
