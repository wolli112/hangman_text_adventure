'''
Galgenmännchen Spiel
https://github.com/wolli112/hangman_text_adventure

MIT License

Copyright (c) 2024 wolli112

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
__version__ = '0.1'
__author__ = 'wolli112'

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
