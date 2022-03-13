import os
import time
os.system("cls")
print("""             \N{sauropod}  KARAR AGACI OYUNU \N{sauropod}\n
******************************************************
  Bu Program Evde Bulunabilen Elektronik Aletleri 
               Tahmin Etmeye Calisir.
******************************************************""")
time.sleep(6)
print("Lütfen cevaplarinizi iyi düsünerek verin.\nKatiliminiz icin simdiden tesekkürler.")
print("*******************************************")
time.sleep(6);os.system("cls");print(3);time.sleep(2);os.system("cls");print(2);time.sleep(2);os.system("cls");print(1);time.sleep(2);os.system("cls")
hzr = input("Hazirsaniz 1'e basin...:")
if hzr == "1":
      os.system("cls")
      while True:
        puan = 100
        ürün = input("Elektronik mi? y/n  :")
        if ürün == "y" :
              cevap = input("Mutfak Esyalarindan mi? y/n  :");time.sleep(1); puan -= 5
              if cevap == "y" :
                    cevap = input("Tasinabilir mi? y/n  :");time.sleep(1); puan -= 5
                    if cevap == "y" :
                        cevap = input("Isitma özelligi var mi? y/n  :");time.sleep(1); puan -= 5                          
                        if cevap == "y" :
                            cevap = input("Su kullaniyor mui? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                cevap = input("Icine un koyuluyor mu? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                    print("Tahminim...")
                                    time.sleep(2)
                                    print("\N{cat} Ekmek Yapma Makinasi \N{cat} , Tahmin Puanim:",puan)
                                    time.sleep(2)
                                else:
                                    cevap = input("Icine süt koyuluyor mu? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Kahve Makinasi \N{cat} , Tahmin Puanim:",puan) 
                                    else:
                                        cevap = input("Icine cay koyuluyor mu? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                            print("Tahminim...")
                                            time.sleep(2)
                                            print("\N{cat} Semaver \N{cat} , Tahmin Puanim:",puan)
                                        else:
                                            print("Tahminim...")
                                            time.sleep(2)
                                            print("\N{cat} Kettle \N{cat} , Tahmin Puanim:",puan)
                            else:
                                cevap = input("Yemek Isitiyor mu? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                    print("Tahminim...")
                                    time.sleep(2)
                                    print("\N{cat} Mikro Dalga Firin \N{cat} , Tahmin Puanim:",puan) 
                                else:
                                      cevap = input("Unlu mamül ile mi kullaniliyor? y/n  :");time.sleep(1); puan -= 5
                                      if cevap == "y":
                                        puan -= 5
                                        cevap = input("Kapagi var mi? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                          print("Tahminim...")
                                          time.sleep(2)
                                          print("\N{cat} Tost Makinasi \N{cat} , Tahmin Puanim:",puan)
                                        else:
                                            print("Tahminim...")
                                            time.sleep(2)
                                            print("\N{cat} Ekmek Kizartma Makinasi \N{cat} , Tahmin Puanim:",puan)
                                      else:
                                          cevap = input("Yag ile  kullaniliyor? y/n  :");time.sleep(1); puan -= 5
                                          if cevap == "y" :
                                              cevap = input("Kizartma Yapiyor mu y/n ");time.sleep(1); puan -= 5
                                              if cevap == "y" :
                                                  print("Tahminim...")
                                                  time.sleep(2)
                                                  print("\N{cat} Fritöz \N{cat} , Tahmin Puanim:",puan)
                                              else:
                                                  print("Tahminim...")
                                                  time.sleep(2)
                                                  print("\N{cat} Misir Patlatma Makinasi \N{cat} , Tahmin Puanim:",puan)
                                          else:
                                                  print("Tahminim...")
                                                  time.sleep(2)
                                                  print("\N{cat} Yogurt Yapma Makinasi\N{cat} , Tahmin Puanim:",puan)
                        else:
                            cevap = input("Kesici Özelligi var mi? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                              print("Tahminim...")
                              time.sleep(2)
                              print("\N{cat} Mixer & Blender \N{cat} , Tahmin Puanim:",puan)
                            else:
                              cevap = input("Kesici Özelligi var mi? y/n  :");time.sleep(1); puan -= 5
                              if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Meyva Sikacagi \N{cat} , Tahmin Puanim:",puan)
                              else:
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Dondurma Mk. \N{cat} , Tahmin Puanim:",puan)
                    else:
                        cevap = input("Isitma islemi yapabiliyor mu? y/n  :");time.sleep(1); puan -= 5
                        if cevap == "y" :
                          cevap = input("Yikama yapabiliyor mu? y/n  :");time.sleep(1); puan -= 5
                          if cevap == "y" :
                            print("Tahminim...")
                            time.sleep(2)
                            print("\N{cat} Bulasik makinasi \N{cat} , Tahmin Puanim:",puan)
                          else:
                              print("Tahminim...")
                              time.sleep(2)
                              print("\N{cat} Firin \N{cat} , Tahmin Puanim:",puan)
                        else:
                            cevap = input("Genellikle 2 Kapakli mi? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Buzdolabi \N{cat} , Tahmin Puanim:",puan)
                            else:
                              print("Tahmin hakkimi kullaniyorum")
                              print("\N{cat} Derin Dondurucu \N{cat} , Tahmin Puanim:",puan)
                              cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                              if cevap == "y" :
                                print("Tesekkurler")
                              else:
                                print("O zaman Aspiratör olmali, Tahmin Puanim:",puan)
              else:
                  cevap = input("Film izlenebilir mi? y/n  :");time.sleep(1); puan -= 5
                  if cevap == "y" :
                      cevap = input("Elde tutularak mi kullanilir? y/n  :");time.sleep(1); puan -= 5
                      if cevap == "y" :
                        cevap = input("Arama yapabiliyor  mu? y/n  :");time.sleep(1); puan -= 5
                        if cevap == "y" :
                            cevap = input("Asil amaci arama yapmak mi? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Telefon \N{cat} , Tahmin Puanim:",puan)
                            else:
                                cevap = input("Kola mi takilir? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                    print("Tahminim...")
                                    time.sleep(2)
                                    print("\N{cat} Akilli Saat \N{cat} , Tahmin Puanim:",puan)
                                else:
                                    print("Tahmin hakkimi kullaniyorum")
                                    print("\N{cat} Akilli Telefon \N{cat} , Tahmin Puanim:",puan)
                                    cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                      print("Tesekkurler")
                                    else:
                                      print("O zaman Tablet olmali, Tahmin Puanim:",puan)
                        else:
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Video Kamera \N{cat} , Tahmin Puanim:",puan)
                      else:
                            cevap = input("Matematiksel islem yapilabilir mi? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Bilgisayar \N{cat} , Tahmin Puanim:",puan)
                            else:
                              cevap = input("Tek basina kullanilabilir mi? y/n  :");time.sleep(1); puan -= 5
                              if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Televizyon \N{cat} , Tahmin Puanim:",puan)
                              else:
                                cevap = input("Mercegi var mi? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                    print("Tahminim...")
                                    time.sleep(2)
                                    print("\N{cat} Projeksiyon \N{cat} , Tahmin Puanim:",puan)
                                else:
                                    print("Tahmin hakkimi kullaniyorum")
                                    print("\N{cat} Ekran \N{cat} , Tahmin Puanim:",puan)
                                    cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                      print("Tesekkurler")
                                    else:
                                      print("O zaman DVD Player olmali, Tahmin Puanim:",puan)
                  else:
                      cevap = input("Tasinabilir mi? y/n  :");time.sleep(1); puan -= 5
                      if cevap == "y" :
                        cevap = input("Ekrana ihtiyaci var mi? y/n  :");time.sleep(1); puan -= 5
                        if cevap == "y" :
                            cevap = input("Icine Dosya Kopyalanabiliyor mu? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                print("Tahmin hakkimi kullaniyorum")
                                print("\N{cat} Data Storage\N{cat} , Tahmin Puanim:",puan)
                                cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                  print("Tesekkurler")
                                else:
                                  print("O zaman PS olmali")
                            else:
                                cevap = input("Bir sey mi ölcüyor? y/n  :");time.sleep(1); puan -= 5
                                if cevap == "y" :
                                    puan -= 5
                                    cevap = input("Ölcerken zaman kullaniyor mu ? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                        print("Tahmin hakkimi kullaniyorum")
                                        print("\N{cat} Saat\N{cat} , Tahmin Puanim:",puan)
                                        cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                          print("Tesekkurler")
                                        else:
                                          print("O zaman Tansiyon Aleti olmali")
                                    else:
                                      print("Tahminim...")
                                      time.sleep(2)
                                      print("\N{cat} Tarti \N{cat} , Tahmin Puanim:",puan)
                                else:
                                    cevap = input("Yapim amaci yazi yazmak mi? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                      print("Tahminim...")
                                      time.sleep(2)
                                      print("\N{cat} Klavye \N{cat} , Tahmin Puanim:",puan)
                                    else:
                                        print("Tahmin hakkimi kullaniyorum")
                                        print("\N{cat} Mouse \N{cat} , Tahmin Puanim:",puan)
                                        cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                          print("Tesekkurler")
                                        else:
                                          print("O zaman Oyun Konsolu olmali")
                        else:
                            cevap = input("Bilgisayara baglanabiliyor mu? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                    cevap = input("Telefona ihtiyaci var mi? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" : 
                                      print("Tahminim...")
                                      time.sleep(2)
                                      print("\N{cat} Fax \N{cat} , Tahmin Puanim:",puan)
                                    else:
                                      cevap = input("Kagit kullaniyor mu? y/n  :");time.sleep(1); puan -= 5
                                      if cevap == "y" : 
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Printer \N{cat} , Tahmin Puanim:",puan)
                                      else:
                                        print("Tahmin hakkimi kullaniyorum")
                                        print("\N{cat} Hoparlör-Kulaklik\N{cat} , Tahmin Puanim:",puan)
                                        cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                          print("Tesekkurler")
                                        else:
                                          print("O zaman Adaptör olmali")
                            else:
                                  cevap = input("Isitma özelligi var mi? y/n  :");time.sleep(1); puan -= 5
                                  if cevap == "y" :
                                    cevap = input("Her mevsim kullanilabilir mi? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                      cevap = input("Elbise ile mi kullaniliri? y/n  :");time.sleep(1); puan -= 5
                                      if cevap == "y" :
                                          print("Tahminim...")
                                          time.sleep(2)
                                          print("\N{cat} Ütü \N{cat} , Tahmin Puanim:",puan)
                                      else:
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Sac Kurutma Makinasi \N{cat} , Tahmin Puanim:",puan)
                                    else:
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Isitici \N{cat} , Tahmin Puanim:",puan)
                                  else:
                                    cevap = input("Serinletir mi? y/n  :");time.sleep(1); puan -= 5
                                    if cevap == "y" :
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Vantilatör \N{cat} , Tahmin Puanim:",puan)
                                    else:
                                      cevap = input("Temizlik icin mi kullanilir? y/n  :");time.sleep(1); puan -= 5
                                      if cevap == "y" :
                                        print("Tahminim...")
                                        time.sleep(2)
                                        print("\N{cat} Süpürge \N{cat} , Tahmin Puanim:",puan)
                                        cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                        if cevap == "y" :
                                          print("Tesekkurler")
                                        else:
                                          print("O zaman Dis Fircasi olmali")
                                        cevap = input("Cevap yine mi yanlis? y/n  :");time.sleep(1); puan -= 5
                                        print("O zaman kesinlikle Tras Aleti,Tahmin Puanim:",puan)
                                      else:
                                          print("Tahmin hakkimi kullaniyorum")
                                          print("\N{cat} Kumanda \N{cat} , Tahmin Puanim:",puan)
                                          cevap = input("Cevabim dogru mu? y/n  :");time.sleep(1); puan -= 5
                                          if cevap == "y" :
                                            print("Tesekkurler")
                                          else:
                                            print("O zaman Sarj Aleti olmali")   
                      else:
                            cevap = input("Sogutma özelligi var mi? y/n  :");time.sleep(1); puan -= 5
                            if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Klima \N{cat}")
                            else:
                              cevap = input("Kurutma özelligi var mi? y/n  :");time.sleep(1); puan -= 5
                              if cevap == "y" :
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Camasir Kurutma Makinasi \N{cat}  ,Tahmin Puanim:",puan)
                              else:
                                print("Tahminim...")
                                time.sleep(2)
                                print("\N{cat} Camasir Makinasi \N{cat} , Tahmin Puanim:",puan)             
        time.sleep(2)
        if ürün== "n" :
              tekrar = input("Secilen ürün elektronik degil\nTekrar Oynamak icin 1'e Oyundan Cikmak icin 2 tusuna basin.")
              if tekrar =="1":
                continue
              else:
                print("Katiliminiz icin tesekkurler...")
                time.sleep(2)
                break
        else:
              print("Katiliminiz icin tesekkurler...")
              time.sleep(2)
              break
else:
  print("1 tusu sol yukarida yada sag tarafta mevcuttur...")
  time.sleep(3)