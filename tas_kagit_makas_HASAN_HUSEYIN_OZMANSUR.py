import random

def tas_kagit_makas_HASAN_HUSEYIN_OZMANSUR():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları: Taş makası yener, Makas kağıdı yener, Kağıt taşı yener.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    
    secenekler = ["taş", "kağıt", "makas"]
    devam_secenekleri = ["evet", "hayır"]
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0
    
    while True:
        tur_sayisi = 0
        oyuncu_tur_galibiyeti = 0
        bilgisayar_tur_galibiyeti = 0
        
        while oyuncu_tur_galibiyeti < 2 and bilgisayar_tur_galibiyeti < 2:
            oyuncu_secimi = input("Taş, Kağıt, Makas? ").lower()
            
            if oyuncu_secimi not in secenekler:
                print("Geçersiz bir seçim yaptınız. Lütfen taş, kağıt veya makas seçin.")
                continue
            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Turu kazandınız!")
                oyuncu_tur_galibiyeti += 1
            else:
                print("Bilgisayar turu kazandı!")
                bilgisayar_tur_galibiyeti += 1
            
            tur_sayisi += 1
            print(f"Tur Sonuçları: Oyuncu {oyuncu_tur_galibiyeti}, Bilgisayar {bilgisayar_tur_galibiyeti}")
        
        if oyuncu_tur_galibiyeti == 2:
            print("Oyunu kazandınız!")
            oyuncu_galibiyetleri += 1
        else:
            print("Bilgisayar oyunu kazandı!")
            bilgisayar_galibiyetleri += 1
        
        # Oyuncunun devam isteği
        devam_istegi_oyuncu = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        
        # Bilgisayarın devam isteği
        devam_istegi_bilgisayar = random.choice(devam_secenekleri)
        print(f"Bilgisayar devam etmek istiyor mu? {devam_istegi_bilgisayar}")
        
        # Oyunun devam edip etmeyeceğini kontrol et
        if devam_istegi_oyuncu != "evet" or devam_istegi_bilgisayar != "evet":
            print(f"Sonuçlar: Oyuncu {oyuncu_galibiyetleri} galibiyet, Bilgisayar {bilgisayar_galibiyetleri} galibiyet")
            print("Oyunu bitirdiğiniz için teşekkür ederiz!")
            break

# Fonksiyonu çağırıyoruz
tas_kagit_makas_HASAN_HUSEYIN_OZMANSUR()