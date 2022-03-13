import os
import time
os.system("cls")
liste = ["Firin","Printer","Tost Mk.","Bulasik Mk.","PS4","Camasir Mk.","Buzdolabi","TV","Telefon","Klima"]
print("""      \N{sauropod}  KARAR AGACI OYUNU \N{sauropod}\n
************************************\n
* Lütfen Listeden Bir Ürün Secin  *\n
************************************\n""")
print("\N{ghost} LISTE \N{ghost}")
for i in liste:
  print(i)
while True:
    ürün = input("Elektronik mi? y/n  :")
    if ürün == "y" :
          cevap = input("Kapagi var mi? y/n  :")
          if cevap == "y" :
                time.sleep(1)
                cevap = input("Tasinabilir mi? y/n  :")
                if cevap == "y" :
                    time.sleep(1)
                    cevap = input("Pisirme Özelligi var mi? y/n  :")
                    if cevap == "y" :
                        time.sleep(1)
                        print("Tahminim...")
                        time.sleep(2)
                        print("\N{cat} Tost Mk. \N{cat}") 
                    else:
                        time.sleep(1)
                        print("Tahminim...")
                        time.sleep(2)
                        print("\N{cat} Printer \N{cat}") 
                else:
                      cevap = input("Icine Tabak-Canak koyulur mu? y/n  :")
                      if cevap == "y" :
                          cevap = input("Isitir mi? y/n  :")
                          if cevap == "y" :
                            cevap = input("Yikar mi? y/n  :")
                            if cevap == "y" :
                                time.sleep(1)
                                print("Tahminim...")
                                time.sleep(1)
                                print("\N{cat} Bulasik Mk. \N{cat}")
                                time.sleep(2)            
                            else:
                                time.sleep(1)
                                print("Tahminim...")
                                time.sleep(1)
                                print("\N{cat} Firin \N{cat}")
                                time.sleep(2)
                          else:
                            time.sleep(1)
                            print("Tahminim...")
                            time.sleep(1)
                            print("\N{cat} Buzdolabi \N{cat}")
                            time.sleep(2)
                      else:
                        time.sleep(1)
                        print("Tahminim...")
                        time.sleep(1)
                        print("\N{cat} Camasir Mk. \N{cat}")
                        time.sleep(2)
          else:
                  cevap = input("Kumandasi var mi? y/n  :")
                  if cevap == "y" :
                      cevap = input("Serinletir mi? y/n  :")
                      if cevap == "y" :
                          time.sleep(1)
                          print("Tahminim...")
                          time.sleep(1)
                          print("\N{cat} Klima \N{cat}")
                          time.sleep(2)
                      else:
                          cevap = input("Ekrani var mi? y/n  :")
                          if cevap == "y" :
                              time.sleep(1)
                              print("Tahminim...")
                              time.sleep(1)
                              print("\N{cat} TV \N{cat}")
                              time.sleep(2)
                          else:
                              time.sleep(1)
                              print("Tahminim...")
                              time.sleep(1)
                              print("\N{cat} PS4\N{cat}")
                              time.sleep(2)
                  else:
                      time.sleep(1)
                      print("Tahminim...")
                      time.sleep(1)
                      print("\N{cat} Telefon \N{cat}")
                      time.sleep(2)

    if ürün== "n" :
          print("Secilen ürün elektronik degil\nOyundan cikmak icin y/n disinda herhangi bir tusa basin.")
    else:
          print("Katiliminiz icin tesekkurler...")
          time.sleep(2)
          break


      
        









    #nesne = input("Aklinizdan bir nesne tutun:")
