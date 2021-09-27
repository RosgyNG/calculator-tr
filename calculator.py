import os
import time

import colorama
from colorama import Fore, Style

colorama.init()


def menu():
    print(Fore.BLUE + "Ne tür işlem yapmak istersin?" + Style.RESET_ALL)
    selection = input(
        Fore.GREEN + "1. Toplama \n2. Çıkarma \n3. Çarpma \n4. Bölme \n5. Küpe Dönüştürme \n" + Fore.LIGHTBLUE_EX + "Numara (1-4) yazınız: ")
    if selection == str(1):
        toplama()
    elif selection == str(2):
        cikarma()
    elif selection == str(3):
        carpma()
    elif selection == str(4):
        bolme()
    elif selection == str(5):
        kupe_donusturme()

    elif selection == str():
        print("Lütfen bir numara yazınız.(1-4)")
        time.sleep(2)
        os.system('cls||clear')
        menu()
    else:
        print("Yanlış numara girildi. Lütfen tekrar deneyiniz.")
        time.sleep(2)
        os.system('cls||clear')
        menu()


def toplama():
    x = input("İlk sayıyı yaz: ")
    y = input("İkinci sayıyı yaz: ")
    cevap = int(x) + int(y)
    print("Cevap: " + str(cevap))


def cikarma():
    x = input("İlk sayıyı yaz: ")
    y = input("İkinci sayıyı yaz: ")
    cevap = int(x) - int(y)
    print("Cevap: " + str(cevap))


def carpma():
    x = input("İlk sayıyı yaz: ")
    y = input("İkinci sayıyı yaz: ")
    cevap = int(x) * int(y)
    print("Cevap: " + str(cevap))


def bolme():
    x = input("İlk sayıyı yaz: ")
    y = input("İkinci sayıyı yaz: ")
    cevap = int(x) / int(y)
    print("Cevap: " + str(int(cevap)))


def kupe_donusturme():

    def alandan_kupe_donustur(x):    # Karenin alanını küpe dönüştürme
        answer = int(x) * int(x) * int(x)
        print("Cevap: " + str(answer))

    def kenardan_kupe_donustur(x):    # Kenar uzunluğu küpe dönüştürme
        answer = int(x) * int(x)
        print("Cevap: " + str(answer))         

    selection2 = input("\na) Karenin bir kenarınının uzunluğu\nb) Karenin alanı \nNeyi girmek istersiniz? (Seçenek harfi giriniz): ")


    if selection2 == str("a"):
        num1 = input("Lütfen dönüştürmek istediğin karenin bir kenar uzunluğu yazınız: ")
        alandan_kupe_donustur(int(num1))
    elif selection2 == str("b"):
        num1 = input("Lütfen dönüştürmek istediğin karenin alanını yazınız: ")
        kenardan_kupe_donustur(int(num1))



menu()
