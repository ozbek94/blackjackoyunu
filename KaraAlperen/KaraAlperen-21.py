import random
import os
kartlar = [2,3,4,5,6,7,8,9,10,11]
bakiye = 100
clear = lambda: os.system("cls")
print("---------------------------------------")
print ("            ***KARA ALPEREN***")
print("---------------------------------------")
print("\n")
    while True:

        acik_Kart = random.choices(kartlar, k=2)
        rakip_Kart = random.choices(kartlar, k=2)
        rakip_skor = rakip_Kart[0] + rakip_Kart[1]
        sayi = 0
        print("rakip skor : " + str(rakip_skor))

        if bakiye > 0:
            print("Bakiyeniz : " +str(bakiye))
            print("")
            sayi = acik_Kart[0] + acik_Kart[1]
            clear()
            islem = int(input(" Oyuna başlama için '1' e bas : "))

        else:
            print("***GAME OVER***")
            break

        if(islem == 1) :


                print("Kartlarınız : " + str(acik_Kart))



                if sayi == 21 :
                    print("tebrikler KaraALPEREN yaptınız kazandınız")
                    bakiye = bakiye + 50
                elif sayi < 21 :
                    while True :
                        print("Kart çekmek için '1'e sonucu görmek için '2' ye basınız")
                        islem1 = int(input())
                        if islem1 == 1 :
                            yeni_Kart =  random.choices(kartlar, k=1)
                            sayi = sayi + yeni_Kart[0]

                            if sayi > 21 :
                                print("Açılan kart : ")
                                print(yeni_Kart)
                                print("/n Skorunuz : ")
                                print(sayi)
                                print("21' i gectiniz gitti paranız")
                                bakiye = bakiye - 50
                                break
                            else:
                                if sayi == 21:
                                    print("tebrikler KaraALPEREN yaptınız kazandınız")
                                    bakiye = bakiye + 50
                                    break
                                else:
                                    print("Yeni kartınız : ")
                                    print(yeni_Kart)
                                    print(sayi)
                                    if rakip_skor + 2 < 21:
                                        rakip_skor = rakip_skor +2



                        elif islem1 == 2 :
                            print("Skorunuz = " )
                            print(sayi)
                            print("Rakip Skor = ")
                            print(rakip_skor)
                            if rakip_skor < sayi :
                                print("Tebrikler, alın size 50$")
                                bakiye = bakiye + 50
                                break
                            elif rakip_skor == sayi :
                                print("Yenen yok bir dahakine")
                                break
                            else:
                                print("Gitti 50$ ...")
                                bakiye = bakiye - 50
                                break
                        else:
                            print("Geçerli işlem giriniz...")

        else:
            print("baştannn")