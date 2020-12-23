import os
import time

import colorama
from colorama import Fore, Style

colorama.init()


def menu():
    print(Fore.BLUE + "Ne tür işlem yapmak istersin?" + Style.RESET_ALL)
    selection = input(
        Fore.GREEN + "1. Toplama \n2. Çıkarma \n3. Çarpma \n4. Bölme \n" + Fore.LIGHTBLUE_EX + "Numara (1-4) yazınız: ")
    if selection == str(1):
        toplama()
    elif selection == str(2):
        cikarma()
    elif selection == str(3):
        carpma()
    elif selection == str(4):
        bolme()
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


menu()
