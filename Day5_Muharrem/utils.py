# ================================================
# utils.py — Yardımcı Araçlar Modülü
# GÜN 5 — Modüller & Hata Yönetimi
# ================================================

import os

LOG_FILE = "errors.log"


def guvenli_sayi_al(mesaj):
    """
    Kullanıcıdan güvenli şekilde sayı alır.
    Sayı olmayana kadar tekrar sorar.
    
    try/except burada devreye girer:
    int() dönüşümü başarısızsa ValueError yakalanır.
    """
    while True:
        try:
            deger = float(input(f"  {mesaj}: "))
            return deger
        except ValueError:
            print("  ⚠️  Geçersiz giriş! Lütfen bir sayı girin.")


def hata_logla(islem, hata_mesaji):
    """
    BOOST: Hata mesajını log dosyasına yazar.
    'a' modu: dosyaya ekleme yapar (üzerine yazmaz).
    """
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"İşlem: {islem} | Hata: {hata_mesaji}\n")


def baslik_yazdir(metin):
    """Ekrana başlık formatında yazdırır."""
    print("\n" + "=" * 42)
    print(f"  {metin}")
    print("=" * 42)
