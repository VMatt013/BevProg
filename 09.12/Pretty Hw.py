#!/usr/bin/env python
# coding: utf8

Colors = {'green' : "\033[92m"}

def main():
    g = '\033[92m'
    e = '\033[0m'
    l = '\n'

	#1. Feladat
    txt = input(l + 'Adjon meg egy mondatot:' + g + ' ')
    Lett = {}

    for x in txt.upper().replace(' ',''):
        try:
            Lett[x] += 1
        except:
            Lett[x] = 1

    print("\nBetűk gyakorisága:",Lett,'\n')
    print("Fordítva: ", txt[::-1],'\n')
    print("Listába rendezve szavanként:",txt.split(' '),"\n")

    #2. Feladat

    num ,unit= input("Adjon meg egy számot és egy mértékegységet (cm/inch): ").split(' ')
    num = int(num)



    if unit == "inch":
        print(format(num * 0.393700787,".2f"), "centimeters")
    elif unit == "cm":
        print(format(num * 2.54,".2f"), "inches")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    #print( Colors+ ['green']"hehe" + "\033[0m")
    main()