# ================================================
# GÜN 2 — MİNİ PROJE: Basit Kullanıcı Analiz Aracı
# Konu: String İşlemleri, Listeler, Operatörler
# ================================================

# --- 1. KULLANICIDAN BİLGİ AL ---
print("=" * 42)
print("     KULLANICI ANALİZ ARACI")
print("=" * 42)

isim     = input("İsminizi girin       : ")
soyisim  = input("Soyisminizi girin    : ")
yas      = int(input("Yaşınızı girin       : "))

print("\nEn sevdiğin 3 teknolojiyi gir:")
teknoloji1 = input("  Teknoloji 1 : ")
teknoloji2 = input("  Teknoloji 2 : ")
teknoloji3 = input("  Teknoloji 3 : ")

# --- 2. STRING İŞLEMLERİ ---
# Birleştirme (concatenation)
tam_isim         = isim + " " + soyisim

# Büyük harfe çevirme
tam_isim_buyuk   = tam_isim.upper()

# İsmin karakter sayısı
isim_uzunlugu    = len(isim)

# --- 3. LİSTE OLUŞTUR ---
teknoloji_listesi = [teknoloji1, teknoloji2, teknoloji3]

# Teknoloji sayısı
teknoloji_sayisi  = len(teknoloji_listesi)

# --- 4. OPERATÖRLERİ KULLAN ---
# Karşılaştırma operatörü: yaş 18'den büyük mü?
yas_durumu = "Yazılım yolculuğuna hazırsın " if yas >= 18 else "Erken başladın, bu çok iyi ⚡"

# Mantıksal operatör: tam 3 teknoloji girildi mi?
teknoloji_durumu = "Keşfetmeye açıksın " if teknoloji_sayisi == 3 else "Listeyi genişletebilirsin 📚"

# --- 5. RAPORU YAZDIR ---
print()
print("=" * 42)
print("       KULLANICI ANALİZ RAPORU")
print("=" * 42)
print(f"  İsim Soyisim      : {tam_isim_buyuk}")
print(f"  İsim Uzunluğu     : {isim_uzunlugu} karakter")
print(f"  Yaş               : {yas}")
print("-" * 42)
print(f"  Sevdiğin Teknolojiler :")
for i, teknoloji in enumerate(teknoloji_listesi, start=1):
    print(f"    {i}. {teknoloji}")
print(f"  Toplam Teknoloji  : {teknoloji_sayisi}")
print("-" * 42)
print("  DURUM:")
print(f"    → {yas_durumu}")
print(f"    → {teknoloji_durumu}")
print("=" * 42)

# --- BOOST: Yaşa göre ek mesajlar ---
print("\n  DETAYLI DEĞERLENDİRME:")
if yas < 18:
    print("   Genç bir yazılımcısın, avantajın bu!")
elif yas >= 18 and yas <= 25:
    print("   En verimli öğrenme çağındasın!")
elif yas > 25 and yas <= 35:
    print("   Deneyim + öğrenme = güçlü kombinasyon!")
else:
    print("   Yazılıma başlamak için geç yoktur!")
print("=" * 42)

# ================================================
# ÖĞRENME NOTLARI:
#   - String: metin; .upper(), .lower(), len() ile işlenir
#   - Liste: birden fazla veriyi tek değişkende tutar
#   - Operatörler: >, <, == karşılaştırır; and/or mantık kurar
#   - Aritmetik (+): sayıları toplar, stringleri birleştirir
# ================================================
