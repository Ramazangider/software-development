while True:


    girdi1 = int(input(" ilk sayiyi giriniz ;"))

    girdi2 = int(input(" ikinci sayiyi giriniz ;"))

    def topla(girdi1, girdi2):
        sonuç = girdi1 + girdi2
        print(sonuç)

    def çikar(girdi1, girdi2):
        sonuç = girdi1 - girdi2
        print(sonuç)

    def çarp(girdi1, girdi2):
        sonuç = girdi1 * girdi2
        print(sonuç)

    def böl(girdi1, girdi2):
        sonuç = girdi1 / girdi2
        print(sonuç)

    print("toplama için 1 ;")
    print("çikarma için 2 ;")
    print("çarpma için 3 ;")
    print("bölme için 4 ;")

    işlem = int(input("işlem seçiniz ; "))
    if işlem == 1:
        topla(girdi1, girdi2)

    elif işlem == 2:
        çikar(girdi1, girdi2)

    elif işlem == 3:
        çarp(girdi1, girdi2)

    elif işlem == 4:
        böl(girdi1, girdi2)

    else :
        print("lütfen tekrar deneyin")