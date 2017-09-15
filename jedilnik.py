#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Vnesi jedilnik"
#definiram spremenljivko dictionary
jedilnik={}
#dobim input za dva seznama
while True:
    jed = raw_input("Kakšen je danes meni? :")
    cena = raw_input("Kolikšna je cena menija? ")

    jedilnik[jed] = cena

    newTask=raw_input("Želiš vnesti še kaj?: (Da/Ne)").lower()
    if newTask == "ne":
        break

#print jedilnik

jedilnik_file = open("meni.txt", "w+")

#print "Seznam jedi "

jedilnik_file.write("Jedilnik: \n")
jedilnik_file.write("Meni:..........|...........Cena \n")

for jed in jedilnik:
       # print jed
        jedilnik_file.write("* " + jed + "................cena: " + cena + "\n")

print "END"