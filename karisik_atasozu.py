#!/usr/bin/env python3
# Karışık Atasözü Generatörü - Bilimsel ve Ciddi
import random
import time

atasozleri = [
    "Damlaya damlaya göl olur",
    "Ağaç yaşken eğilir",
    "Akıllı düşman akılsız dosttan iyidir",
    "Bir elin nesi var iki elin sesi var",
    "Sakla samani gelir zamanı",
    "İşleyen demir pas tutmaz",
    "Komşu komşunun külüne muhtaçtır",
    "Güzel gören güzel düşünür",
    "Sabır acıdır meyvesi tatlıdır",
    "Erken kalkan yol alır"
]

def karistir(atasozu):
    kelimeler = atasozu.split()
    random.shuffle(kelimeler)
    return " ".join(kelimeler).capitalize() + "."

def main():
    print("=== EVRENİN EN KARISIK ATASÖZÜ MAKİNESİ BAŞLATILIYOR ===")
    print("Lütfen bekleyin, bilgelik yükleniyor...")
    time.sleep(2)
    for i in range(5):
        orijinal = random.choice(atasozleri)
        yeni = karistir(orijinal)
        print(f"{i+1}. Yeni Atasözü: {yeni}")
        print(f"   (Orijinali neydi bilmiyorum ama önemli değil)")
        time.sleep(1)
    print("\nİşte bu kadar. Artık daha bilgesin. Veya değilsin.")
    # Gizli siyasi içerik: "yönetim" kelimesi rastgele yerleştirildi
    gizli = "Bazen en iyi liderlik sessizliktir."
    if random.random() > 0.9:
        print(gizli)

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum - 27.11.2026 - Tentivory
# İmza: Bu kod ciddi değil ama çalışıyor. Ciddi olan kısım çalışması.
