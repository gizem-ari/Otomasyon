#Seyehat Otomasyonu

durum = "x"  # prime durum tanımlanmamış(güncellenmemiş)
musteri_no = " "
bilgiler = dict()
bilet_sayi = 0


def ekleme():
    ilk_no = 100
    with open("21100011007_id.txt", "r") as file:
        idd = file.readlines()
    idd.sort()
    for i in range(len(idd)):
        if str(ilk_no) in idd[i]:
            ilk_no += 1
        else:

            break
    with open("21100011007_id.txt", "a") as file:
        file.write(str(ilk_no))
        file.write("\n")

    global durum

    ad = input("Müşteri adı:")
    bilgiler["Ad"] = ad
    soyad = input("Müşteri soyadı:")
    bilgiler["Soyad"] = soyad
    cinsiyet = input("Müşteri cinsiyeti:")
    bilgiler["Cinsiyet"] = cinsiyet
    bilet_sayi = 0
    bilgiler["Bilet_sayi"] = bilet_sayi
    musteri_no = str(ilk_no)
    bilgiler["Musteri_no"] = musteri_no

    with open("21100011007_musteri_bilgileri.txt", "a") as file:
        file.write(
            musteri_no + "=" + ad + " " + soyad + " " + cinsiyet + ":" + str(bilet_sayi) + ":" + durum + "\n")
    musteriler.append(bilgiler)
    print("Müşteri numaranız:", musteri_no)


def prime_gunceleme():
    with open("21100011007_id.txt", "r") as file:
        sira = file.read()
        numaralar = sira.split("\n")
    arama = input("Güncellemek istediğiniz müşteri numarasını giriniz:")
    if arama in numaralar:
        with open("21100011007_musteri_bilgileri.txt", "r") as file:
            satir = file.readlines()
            sayac = 0       #hocam bu kısımdaki isimlendirmeler biraz karışık oldu sonradan da değiştiremedim
                            # farklı değişkenler kulanarak detaylı bir dilimleme işlemi yaptım
            for i in satir:  #bu dilimleme sayesinde de istediğim değişkeni kullanabildim ve
                dilim = i.split("=")    #bilgileri doğru şekilde tutup güncelleyebildim
                sayac += 1
                if arama in dilim:
                    gecici = dilim[1]
                    dilim2 = gecici.split(" ")
                    gecici2 = dilim2[2]
                    print("musteri_no:", dilim[0])
                    print("ad:", dilim2[0])
                    print("soyad:", dilim2[1])
                    dilim3 = gecici2.split(":")
                    print("cinsiyet:", dilim3[0])
                    print("bilet sayi:", dilim3[1])
                    bilet_sayi = dilim3[1]
                    print("Prime durumu:", dilim3[2])
                    musteri_no = dilim[0]
                    ad = dilim2[0]
                    soyad = dilim2[1]
                    cinsiyet = dilim3[0]

                    print(
                        "Prime müşteri olabilmek için daha önce aldığınız bilet sayısınız 5 ve 5ten fazla olması gerekli")

                    global durum
                    if int(bilet_sayi) >= 5:
                        durum = "+"  # Prime
                        dilim3[2] = durum
                        print("Tebrikler artık prime müşterisiniz.")
                        guncel = musteri_no + "=" + ad + " " + soyad + " " + cinsiyet + ":" + str(
                            bilet_sayi) + ":" + durum + "\n"

                    else:
                        durum = "-"  # Prime değil
                        dilim3[2] = durum
                        print("Bilet sayınız yeterli değil prime müşteri olamadınız :(")
                        guncel = musteri_no + "=" + ad + " " + soyad + " " + cinsiyet + ":" + str(
                            bilet_sayi) + ":" + durum + "\n"

                    with open("21100011007_musteri_bilgileri.txt", "r+") as file:
                        satirr = file.readlines()
                        file.seek(0)
                        file.truncate()
                        file.writelines(satirr[:sayac - 1])
                        file.writelines(satirr[sayac:])
                        file.close()
                    with open("21100011007_musteri_bilgileri.txt", "r+") as file:
                        guncel_satir = file.readlines()
                        guncel_satir.insert(sayac - 1, guncel)
                        file.seek(0)
                        file.writelines(guncel_satir)

        with open("21100011007_id.txt", "r") as file:
            sira = file.read()
            numaralar = sira.split("\n")
        if arama in numaralar:
            print("Güncel durum:")
            with open("21100011007_musteri_bilgileri.txt", "r") as file:
                satir = file.readlines()
                for gecici in satir:
                    satir2 = gecici.split("=")
                    if arama in satir2:
                        print(satir2[0], satir2[1])

    else:
        print("Yanlış numara girdiniz!")
        prime_gunceleme()


def musteri_arama():
    try:
        with open("21100011007_id.txt", "r") as file:
            sira = file.read()
            numaralar = sira.split("\n")

        arama = input("Aradığınız müşteri numarasını giriniz:")
        if arama in numaralar:
            print("Kullanıcı bulundu.")
            with open("21100011007_musteri_bilgileri.txt", "r") as file:
                satir = file.readlines()
                for gecici in satir:
                    satir2 = gecici.split("=")  # musteri bilgilerini numara ve diger bilgiler olmak üzere 2 parcaya ayırdım
                    if arama in satir2:
                        print("Hesap numarası:{}".format(satir2[0]))
                        print("Bilgiler:", satir2[1])

        else:
            print("Yanlış numara girdiniz!")
            musteri_arama()
    except FileNotFoundError:
        print("Dosya bulunamadı.")


def silme():
    with open("21100011007_id.txt", "r") as file:
        sira = file.read()
        numaralar = sira.split("\n")
    arama = input("Silmek istediğiniz müşteri numarasını giriniz:")
    if arama in numaralar:
        with open("21100011007_musteri_bilgileri.txt", "r") as file:
            satir = file.readlines()
            sayac2 = 0

            for i in satir:
                dilim = i.split("=")
                sayac2 += 1
                if arama in dilim:
                    with open("21100011007_musteri_bilgileri.txt", "r+") as file:
                        satirr = file.readlines()
                        file.seek(0)
                        file.truncate()
                        file.writelines(satirr[:sayac2 - 1])
                        file.writelines(satirr[sayac2:])
                        file.close()
                    with open("21100011007_id.txt", "r+") as file:
                        satirr2 = file.readlines()
                        file.seek(0)
                        file.truncate()
                        file.writelines(satirr2[:sayac2 - 1])
                        file.writelines(satirr2[sayac2:])
                        file.close()
                    print("Müşteri başarıyla silindi")  # müsteriler ve id dosyalarından silme
    else:
        print("Yanlış numara girdiniz!")
        silme()


def bilet_alma():
    def bilet_secim(fiyat, durum):
        global yeni_bilet
        global son_tutar
        indirim = 0
        secim = input("Gidiş-dönüş bilet alımlarında %5 indirim uygulanır.\n"
                      "Gidiş-dönüş bilet çifti almak ister misiniz?(E/H):")

        if secim == "e" or secim == "E":
            yeni_bilet = int(input("Almak istediğiniz bilet çifti sayısı:"))
            if yeni_bilet % 2 == 0:
                indirim = (fiyat * yeni_bilet * 0.05)
            else:
                print("Çift bilet sayıı girmediniz. Yeniden deneyiniz. ")
                bilet_alma()

        elif secim == "h" or secim == "H":
            yeni_bilet = int(input("Almak istediğiniz bilet sayısı:"))
        else:
            print("Hatalı seçim yaptınız.Yeniden deneyiniz.")
            bilet_alma()
        tutar = int((fiyat * yeni_bilet) - indirim)
        print("İlk tutar:", tutar)
        if '+' in durum:
            son_tutar = int(tutar * 0.9)
            print("Prime durumunda olduğunuz için ek indirimden yararlandınız.Ödemeniz gereken tutar:", son_tutar)
        elif '-' in durum:
            son_tutar = tutar
            print("Prime durumunda olmadığınız için ek indirimden yararlanamadınız:( Ödemeniz gereken tutar:",
                  son_tutar)
        elif 'x' in durum:
            print("Prime durumu güncellemesi yapmamışsınız.Güncelleme ekranına yönlendiriliyorsunuz.\n"
                  "Günceleme işleminden sonra bilet alma ekranımız sizi tekrar karşılayacaktır")
            prime_gunceleme()
            print("Bilet alma işlemini yeniden yapınız lütfen")
            bilet_alma()
        print("Lütfen, bilet alma işlemlerinden sonra genel güncelleme işlemini yapın.")
        son_tutar = int(son_tutar)
        return yeni_bilet, son_tutar

    with open("21100011007_id.txt", "r") as file:
        sira = file.read()
        numaralar = sira.split("\n")
    arama = input("İşlem yapmak istediğiniz müşteri numarasını giriniz:")
    if arama in numaralar:
        with open("21100011007_musteri_bilgileri.txt", "r") as file:
            satir = file.readlines()
            sayac = 0
            for i in satir:
                dilim = i.split("=")
                sayac += 1
                if arama in dilim:
                    gecici = dilim[1]
                    dilim2 = gecici.split(" ")
                    gecici2 = dilim2[2]
                    dilim3 = gecici2.split(":")
                    musteri_no = dilim[0]
                    ad = dilim2[0]
                    soyad = dilim2[1]
                    cinsiyet = dilim3[0]
                    bilet_sayi = (dilim3[1])  # dilim değerini görmek için ekledim
                    durum = dilim3[2]

                    print("Acentemizin anlaşmalı olduğu şehirler ve bilet ücretleri aşağıda verildiği gibidir:\n"
                          "1)İstanbul:tren_fiyat=250 otobus_fiyat=220\n"
                          "2)Sakarya:tren_fiyat=200 otobus_fiyat=170\n"
                          "3)Kayseri:otobus_fiyat=100\n"
                          "4)Antalya:otobus_fiyat=200\n"
                          "5)İzmir:tren_fiyat=150\n")
                    sehir = input("Şehir seçimi için yukarıda verilen sayılardan birini girin:")
                    if sehir == '1':
                        arac = input(
                            "İstanbul için tren ve otobüs ulaşımı bulunmaktadır.Tren için t'yi, otobüs için o'yu tuşlayın\n"
                            "Seçiminiz:")
                        if arac == "t" or arac == "T":
                            fiyat = 250
                            print("1 tren bileti fiyatı 250 TL'dir.")

                        if arac == "o" or arac == "O":
                            fiyat = 220
                            print("1 otobüs bileti fiyatı 220 TL'dir.")
                    elif sehir == '2':
                        arac = input(
                            "Sakarya için tren ve otobüs ulaşımı bulunmaktadır.Tren için t'yi, otobüs için o'yu tuşlayın\n"
                            "Seçiminiz:")
                        if arac == "t" or arac == "T":
                            fiyat = 200
                            print("1 tren bileti fiyatı 200 TL'dir.")

                        if arac == "o" or arac == "O":
                            fiyat = 170
                            print("1 otobüs bileti fiyatı 170 TL'dir.")
                    elif sehir == '3':
                        print("Kayseri için otobüs ulaşımı bulunmaktadır.\n"
                              "1 otobüs bileti fiyatı 100 TL'dir.")
                        fiyat = 100
                    elif sehir == '4':
                        print("Antalya için otobüs ulaşımı bulunmaktadır.\n"
                              "1 otobüs bileti fiyatı 200 TL'dir.")
                        fiyat = 200
                    elif sehir == '5':
                        print("İzmir için tren ulaşımı bulunmaktadır.\n"
                              "1 tren bileti fiyatı 150 TL'dir.")
                        fiyat = 150
                    global son_tutar
                    gecici9 = bilet_secim(fiyat, durum)
                    s_tutar = gecici9[1]

                    global yeni_bilet
                    bilet_sayi = int(dilim3[1]) + yeni_bilet
                    # bu kısımdan itibaren yeni değerleri 'guncel'e atama ve dosyaya yazma işlemleri
                    guncel = musteri_no + "=" + ad + " " + soyad + " " + cinsiyet + ":" + str(
                        bilet_sayi) + ":" + durum

                    with open("21100011007_musteri_bilgileri.txt", "r+") as file:
                        satirr = file.readlines()
                        file.seek(0)
                        file.truncate()
                        file.writelines(satirr[:sayac - 1])
                        file.writelines(satirr[sayac:])
                        file.close()
                    with open("21100011007_musteri_bilgileri.txt", "r+") as file:
                        guncel_satir = file.readlines()
                        guncel_satir.insert(sayac - 1, guncel)
                        file.seek(0)
                        file.writelines(guncel_satir)

        with open("21100011007_id.txt", "r") as file:
            sira = file.read()
            numaralar = sira.split("\n")
        if arama in numaralar:
            with open("21100011007_musteri_bilgileri.txt", "r") as file:
                satir = file.readlines()
                for gecici in satir:
                    satir2 = gecici.split("=")
                    #if arama in satir2:
                        # print(satir2[0], satir2[1])

    else:
        print("Yanlış numara girdiniz!")
        bilet_alma()
    # kişi bilgisi ve biletler için ödemiş olduğu tutarı yeni bir dosyada tuttum
    # bir sonraki fonksiyonum değerlendirme için olacak,hiç bilet almamış kullanıcılar değerlendirme yapmasın
    with open("21100011007_odenen_tutarlar.txt", "a") as file:
        file.write(musteri_no + ":" + str(son_tutar) + "\n")


def degerlendirme():
    print("Acentemizi tercih ettiğiniz için teşekkürler.")
    with open("21100011007_odenen_tutarlar.txt", "r") as file:
        sira = file.read()
        numaralar = sira.split("\n")
    with open("21100011007_id.txt", "r") as file:
        sira1 = file.read()
        numaralar1 = sira1.split("\n")
    arama = input("Lütfen müşteri numaranızı giriniz:")
    if arama in numaralar1:
        with open("21100011007_odenen_tutarlar.txt", "r") as file:
            satir = file.readlines()
            sayac = 0
            if arama in numaralar:
                for i in satir:
                    sayac += 1
                    dilim = i.split(":")
                    musteri_no = dilim[0]
                    son_tutar = dilim[1]

        print("Lütfen acentemizin sistemiyle ilgili gelecek olan anket sorularımızı"
              " 0 ile 10 puan arasında değerendiriniz")
        try:
            s1 = int(input("Müşteri ekleme işlemi için puanınz:"))
            s2 = int(input("Müşteri güncelleme işlemi için puanınz:"))
            s3 = int(input("Bilet alma işlemi için puanınz:"))
            s4 = int(input("Bilgilerinizi görüntüleyebildiğiniz arama işlemi için puanınz:"))
            puan = (s1 + s2 + s3 + s4) // 4
            if puan >= 5:
                print("Değerlendirmeniz için teşekkürler.Beklentilerinizi karşılamış olmaktan kıvanç duyuyoruz:)")
                ifade = "mutluyuz :)"
            else:
                print("Değerlendirmeniz için teşekkürler.Size daha iyi hizmet sunabilmek isteriz."
                      "Lütfen bunu sağlayabilmemiz için bizimle iletişime geçin.Tel No:05xxxxxxxxx")
                ifade = "uzgunuz :("

            guncel = musteri_no + ":" + son_tutar + " " + ifade + "\n"
            with open("21100011007_odenen_tutarlar.txt", "r+") as file:
                satirr = file.readlines()
                file.seek(0)
                file.truncate()
                file.writelines(satirr[:sayac - 1])
                file.writelines(satirr[sayac:])
                file.close()
            with open("21100011007_odenen_tutarlar.txt", "r+") as file:
                guncel_satir = file.readlines()
                guncel_satir.insert(sayac - 1, guncel)
                file.seek(0)
                file.writelines(guncel_satir)
            degerlendirme()
        except ValueError:
            print("Geçersiz değer girişi yapıldı. Lütfen sayısal değerler için doğru formatta girin.")

    elif arama in numaralar1:
        print("Daha önce bilet almadığınız için değerlendirme yapamazsınız!")#burada son saatlerde fark edip
    else:                                                    #uğraştığım bi sıkıntı oldu ama stresten daha çok karıştı bu haliyle
        print("Yanlış numara girdiniz!")                      #bırakmak zorunda kaldım


def menu():
    print("---------ARI Seyehat Acentesine Hoş Geldiniz!!!---------")
    print("1.Ekleme\n2.Güncelleme\n3.Arama\n4.Silme\n5.Bilet Alma\n6.Değerlendirme\n7.CIKIS")
    tercih = input("Tercihinizi giriniz:")
    if tercih not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Yanlış tercih yaptınız!!")
        return None
    return tercih

# baslangic
musteriler = []
ilk_no = 100

tercih = None
while tercih != "7":
    tercih = menu()
    if tercih == "7":
        print("ÇIKIŞ YAPILIYOR")
        break
    elif tercih == "1":
        ekleme()

    elif tercih == "2":
        prime_gunceleme()

    elif tercih == "3":
        musteri_arama()

    elif tercih == "4":
        silme()

    elif tercih == "5":
        bilet_alma()

    elif tercih == "6":
        degerlendirme()
