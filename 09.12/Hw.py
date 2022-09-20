#!/usr/bin/env python
# coding: utf8

def main():
	#1. Feladat
    txt = input('Adjon meg egy mondatot: ')
    Lett = {}

    for x in txt:
        try:
            Lett[x] += 1
        except:
            Lett[x] = 1
    print("Betűk gyakorisága:",Lett)
    print(" Fordítva: ", txt[::-1])
    print(" Listába rendezve szavanként:",txt.split(' '))

    #2. Feladat
    num = float(input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n"))
    unit = input()

    print(e,end='')

    if unit == "inch":
        print(format(num * 0.393700787,".2f"), "centimeters")
    elif unit == "cm":
        print(format(num * 2.54,".2f"), "inches")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    main()