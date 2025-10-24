import os

DOSYA_ADI = "gorevler.txt"

def gorevleri_oku():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return [satir.strip() for satir in dosya.readlines()]
    except FileNotFoundError:
        return []

def gorevleri_kaydet(gorevler):
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
    except Exception as e:
        print(f"Hata: Görevler kaydedilirken bir hata oluştu: {e}")

def gorevleri_listele(gorevler):
    if not gorevler:
        print("Henüz eklenmiş bir görev yok.")
    else:
        print("\n--- Görev Listesi ---")
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")
        print("---------------------")

def gorev_ekle(gorevler):
    yeni_gorev = input("Yeni görev girin: ").strip()
    if yeni_gorev == "":
        print("Hata: Boş görev eklenemez.")
    else:
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print("Görev başarıyla eklendi.")

def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    try:
        secim = int(input("Silmek istediğiniz görevin numarasını girin: "))
        if 1 <= secim <= len(gorevler):
            silinen = gorevler.pop(secim - 1)
            gorevleri_kaydet(gorevler)
            print(f"'{silinen}' başarıyla silindi.")
        else:
            print("Hata: Geçersiz görev numarası.")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")

def gorev_duzenle(gorevler):
    gorevleri_listele(gorevler)
    try:
        secim = int(input("Düzenlemek istediğiniz görevin numarasını girin: "))
        if 1 <= secim <= len(gorevler):
            yeni_metin = input("Yeni görev metnini girin: ").strip()
            if yeni_metin == "":
                print("Hata: Boş görev eklenemez.")
            else:
                gorevler[secim - 1] = yeni_metin
                gorevleri_kaydet(gorevler)
                print("Görev başarıyla güncellendi.")
        else:
            print("Hata: Geçersiz görev numarası.")
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")

def ana_menu():
    gorevler = gorevleri_oku()

    while True:
        print("\n--- ANA MENÜ ---")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görev Düzenle")
        print("4. Görev Sil")
        print("5. Çıkış")

        secim = input("Bir seçenek girin (1-5): ").strip()

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Hata: Geçersiz seçim. Lütfen 1-5 arasında bir seçenek girin.")

# Programı başlat
ana_menu()
ü
