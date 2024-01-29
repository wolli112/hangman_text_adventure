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

import turtle

screen = turtle.Screen()
screen.title("Hangman")
screen.setup(width=420, height=400)

zeiger = turtle.Turtle()
zeiger.hideturtle()

def schritt1():
    # Hügel
    zeiger.penup()
    zeiger.setpos(0, -100)
    zeiger.pendown()
    zeiger.left(90)
    zeiger.circle(30, 180)
    
def schritt2():
    #Balken
    zeiger.penup()
    zeiger.setpos(-30, -70)
    zeiger.pendown()
    zeiger.left(180)
    zeiger.forward(150)

def schritt3():
    #Balken 2
    zeiger.right(90)
    zeiger.forward(75)
    
def schritt4():
    #Balken Quer
    zeiger.backward(25)
    zeiger.setpos(-30, 55)
    zeiger.penup()
    zeiger.setpos(45, 80)
    zeiger.pendown()
    
def schritt5():
    #Strik
    zeiger.right(90)
    zeiger.forward(20)
    
def schritt6():
    #Kopf
    zeiger.right(90)
    zeiger.circle(10)
    
def schritt7():
    #Körper
    zeiger.left(90)
    zeiger.penup()
    zeiger.setpos(45, 40)
    zeiger.pendown()
    zeiger.forward(30)
    
def schritt8():
    #linkes Bein
    zeiger.setpos(30, -5)
    zeiger.setpos(45, 10)

def schritt9():
    #rechtes Bein
    zeiger.setpos(60, -5)
    zeiger.setpos(45, 10)
    
def schritt10():
    #linker Arm
    zeiger.left(180)
    zeiger.forward(15)
    zeiger.setpos(30, 30)
    zeiger.setpos(45, 25)
 
def schritt11():
    #rechter Arm
    zeiger.setpos(60, 30)
    
def gesicht():
    #Gesicht zeichnen
    zeiger.penup()
    zeiger.setpos(44, 55)
    zeiger.pendown()
    zeiger.circle(2)
    zeiger.penup()
    zeiger.setpos(50, 55)
    zeiger.pendown()
    zeiger.circle(2)
    zeiger.penup()
    zeiger.setpos(50, 45)
    zeiger.pendown()
    zeiger.circle(4, 180)
    
def gameover():
    #Ende
    zeiger.penup()
    zeiger.setpos(-70, 130)
    zeiger.pendown()
    zeiger.write("Game Over", font=("Verdana",30, "normal"))
    
def gewonnen():
    #Ende
    zeiger.penup()
    zeiger.setpos(-70, 130)
    zeiger.pendown()
    zeiger.write("Gewonnen !", font=("Verdana",30, "normal"))
    



    
    
