# Hangman Game - Main
# Version 4.0
# Wolfgang Strobl

import getpass
from hangman_game import *    #Importiert hangman_game.py
import time

wort = getpass.getpass("Bitte einen Vornamen eingeben: ")

print("Tipp, der Vorname hat "+ str(len(wort)) + " Buchstaben")

eingabe = input("Rate welcher Vorname gemeint ist: ")

zaehler = 0

while eingabe.lower() != wort.lower():
    zaehler = zaehler + 1
    if zaehler == 1:
        schritt1()
    if zaehler == 2:
        schritt2()
    if zaehler == 3:
        schritt3()
    if zaehler == 4:
        schritt4()
    if zaehler == 5:
        schritt5()
    if zaehler == 6:
        schritt6()
    if zaehler == 7:
        schritt7()
    if zaehler == 8:
        schritt8()
    if zaehler == 9:
        schritt9()
    if zaehler == 10:
        schritt10()
    if zaehler == 11:
        schritt11()
        gesicht()
        gameover()
        print("Game Over")
        print("Das richtige Wort wäre " + wort + " gewesen")
        time.sleep(5)
        break
    eingabe = input("Falsch, Rate nochmal: ")
    
if eingabe.lower() == wort.lower():
    print("Glückwunsch, Du hast "+ wort + " erraten!")
    gewonnen()
    time.sleep(5)