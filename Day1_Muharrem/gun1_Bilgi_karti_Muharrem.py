# ================================================
# GÜN 1 — MİNİ PROJE: Bilgi Kartı
# Konu: Değişkenler & Veri Tipleri
# ================================================

# --- Kullanıcı Bilgilerini Tanımla ---
# string: metin verisi
isim = "Muharrem"

# int: tam sayı verisi
yas = 20

# float: ondalıklı sayı verisi
favori_sayi = 8

# bool: True veya False (mantıksal) verisi
yazilimda_yeni_mi = False

# --- Bilgi Kartını Yazdır ---
print("=" * 38)
print("       KULLANICI BİLGİ KARTI")
print("=" * 38)
print(f"  İsim          : {isim}")
print(f"  Yaş           : {yas}")
print(f"  Favori Sayı   : {favori_sayi}")
print(f"  Yazılıma Yeni : {yazilimda_yeni_mi}")
print("=" * 38)

# --- BOOST: Veri tiplerini açıkla ---
print()
print(">>> VERİ TİPİ BİLGİLERİ <<<")
print(f"  '{isim}' değişkeninin tipi    : {type(isim)}")
print(f"  '{yas}' değişkeninin tipi      : {type(yas)}")
print(f"  '{favori_sayi}' değişkeninin tipi : {type(favori_sayi)}")
print(f"  '{yazilimda_yeni_mi}' değişkeninin tipi  : {type(yazilimda_yeni_mi)}")
print("=" * 38)

# --- BOOST: Ekstra bilgi mesajı ---
if yazilimda_yeni_mi:
    print(f"\n  Merhaba {isim}! Yazılım yolculuğuna hoş geldin 🚀")
else:
    print(f"\n  Merhaba {isim}! Tecrübeni bizimle paylaş 💡")
print("=" * 38)

# ================================================
# ÖĞRENME NOTLARI:
#   - Değişken: bilgiyi saklamak için kullanılan isimli kutu
#   - String (str): metin, tırnak içinde yazılır
#   - Integer (int): tam sayı
#   - Float: ondalıklı sayı
#   - Boolean (bool): True ya da False
#   - print(): bilgiyi ekrana yazdırır
# ================================================
