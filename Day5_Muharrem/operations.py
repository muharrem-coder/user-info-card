# ================================================
# operations.py — Matematiksel İşlemler Modülü
# GÜN 5 — Modüller & Hata Yönetimi
# ================================================

def topla(a, b):
    """İki sayıyı toplar ve sonucu döndürür."""
    return a + b


def cikar(a, b):
    """Birinci sayıdan ikinciyi çıkarır."""
    return a - b


def carp(a, b):
    """İki sayıyı çarpar."""
    return a * b


def bol(a, b):
    """
    İki sayıyı böler.
    Sıfıra bölme durumunda ZeroDivisionError fırlatır.
    """
    if b == 0:
        raise ZeroDivisionError("Bir sayı sıfıra bölünemez!")
    return a / b


# BOOST: Üs alma
def us_al(a, b):
    """a'nın b'inci kuvvetini hesaplar."""
    return a ** b


# BOOST: Mod alma
def mod_al(a, b):
    """a'yı b'ye böldüğündeki kalanı verir."""
    if b == 0:
        raise ZeroDivisionError("Mod işleminde bölen sıfır olamaz!")
    return a % b
