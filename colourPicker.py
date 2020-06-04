#Sophie Jones 03/06/2020
#Colour Picker for Feral Avatars

import csv
from random import randint, choice
import turtle
import re

#list of colours in theme

def start():
    dyes = load_colours()
    #setting up turtle at top left of window
    turtle.setup(800,800)
    turtle.title("Feral Dye Colour Theme Creator")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-390,-380)
    t.pendown()
    t.write("Click on a colour to get a different one.\nPress ENTER for a new theme.\nby @Eurydice on Fer.al Discord",True, align="Left")
    t.penup()
    t.goto(-400,400)
    t.pendown()
    colourNum = 43
    while True:
        main(dyes,t,colourNum)

def load_colours():
    #convert csv to a list of lists
    with open('FeralDyes.csv', 'r') as file:
        reader = csv.reader(file)
        dyes = list(reader)
        dyes.pop(0)
    return dyes

def main(dyes,t,colourNum):
    while colourNum >42:
        colourNum = int(turtle.numinput("INPUT","How many colours would you like?"))
        if colourNum == 2:
            picker = colourPick(colourNum, dyes)
            cType = turtle.textinput("INPUT","Complementary or random?")
            if re.search("c(omplementary)?",cType):
                colours = picker.complementary(picker)
            else:
                picker.nList = picker.cList
                colours = picker.random()
        elif colourNum == 3:
            picker = colourPick(colourNum, dyes)
            cType = turtle.textinput("INPUT","Triadic, analogus, split-complementary or random?")
            cType = cType.lower()
            if re.search("t(riadic)?",cType):
                colours = picker.triadic(picker)
            elif re.search("a(nalogus)?",cType):
                colours = picker.analogus(picker)
            elif re.search("s(plit-complementary)?",cType):
                colours = picker.splitComplementary(picker)
            else:
                picker.nList = picker.cList
                colours = picker.random()
        elif colourNum == 4:
            picker = colourPick(colourNum, dyes)
            cType = turtle.textinput("INPUT","Square or random?")
            if re.search("s(quare)?",cType):
                colours = picker.square(picker)
            else:
                picker.nList = picker.cList
                colours = picker.random()
        elif colourNum > 43:
            print("Number must be lower than 43.")
                
        else:
            picker = colourPick(colourNum, dyes)
            picker.nList = picker.cList
            colours = picker.random()

    side = 200
    n = 1
    t1 = turtle.Turtle()
    t1.hideturtle()
        
    drawSquare(t,t1,colours,100)

    if len(picker.nList) >= 2:
        turtle.listen()
        turtle.onscreenclick(picker.onLeftClick,1)

        turtle.onkey(new, 'Return')
        turtle.mainloop()
    else:
        turtle.listen()
        turtle.onscreenclick(print("No more options"),1)

        turtle.onkey(new, 'Return')
        turtle.mainloop()
    
def new():
    answer = turtle.textinput("INPUT","Would you like another theme?")
    answer = answer.lower()
    if re.search("y(es)?",answer):
        turtle.clearscreen()
        start()
        

def drawSquare(t,t1,colours,side):
    n=1
    for i in range(len(colours)):
        #stopping at end of row
        if (t.xcor()+side) > 400:
            t.penup()
            t.goto(-400,(400-(n*side)))
            t.pendown()
            n+=1
        #drawing square
        t.begin_fill()
        t.color(colours[i][1])
        for x in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()
        #write text
        if colours[i][0]== "White" or colours[i][0]== "Off-White":
            t1.color = "black"
        else:
            t1.color = "white"
        t1.penup()
        t1.goto(t.xcor()+5,(t.ycor()-50))
        t1.pendown()
        t1.write(f"""{colours[i][0]}
    {colours[i][1]}
    {colours[i][2]}""",True,align="left")
        t.forward(side)

class colourPick():
    def __init__(self, colourNum, cList):
        self.colourNum = colourNum
        self.cList = cList
        self.theme = []
        self.nList = []

        #pick first colour
        n = randint(1,len(self.cList)-1)
        self.theme.append(self.cList[n])
        self.cList.pop(n)

    def complementary(self,picker):
        
        #stopping comparisons being over 12
        x = int(self.theme[0][3])
        if x+6 >12:
            y = x-6
        else:
            y = x+6

        #add desired possibilities to nList
        for i in range(len(self.cList)):
            if int(self.cList[i][3]) == y:
                self.nList.append(self.cList[i])

        #use nList to pick 1 more colours
        self.theme = picker.random()
        return (self.theme)

    def splitComplementary(self,picker):
        
        #stopping comparisons being over 12
        x = int(self.theme[0][3])
        if x+5 >12:
            y = x-5
            z = x-7
        elif x+7 >12:
            y = x+5
            z = x-7
            if z<0:
                z = 12+z
        else:
            y = x+5
            z = x+7

        #add desired possibilities to nList
        for i in range(len(self.cList)):
            if int(self.cList[i][3]) == y or int(self.cList[i][3]) == z:
                self.nList.append(self.cList[i])

        #use nList to pick 2 more colours
        self.theme = picker.random()
        return (self.theme)

    def analogus(self,picker):
        
        #stopping comparisons being over 12
        x = int(self.theme[0][3])
        if x+1 >12:
            y = x-1
            z = x-2
        elif x+2 >12:
            y = x+1
            z = x-1
        else:
            y = x+1
            z = x+2

        #add desired possibilities to nList
        for i in range(len(self.cList)):
            if int(self.cList[i][3]) == y or int(self.cList[i][3]) == z:
                self.nList.append(self.cList[i])

        #use nList to pick 2 more colours
        self.theme = picker.random()
        return (self.theme)
        
    def triadic(self,picker):
        
        #stopping comparisons being over 12
        x = int(self.theme[0][3])
        if x+4 >12:
            y = x-4
            z = x-8
        elif x+8 >12:
            y = x+4
            z = x-4
        else:
            y = x+4
            z = x+4

        #add desired possibilities to nList
        for i in range(len(self.cList)):
            if int(self.cList[i][3]) == y or int(self.cList[i][3]) == z:
                self.nList.append(self.cList[i])

        #use nList to pick 2 more colours
        self.theme = picker.random()
        return (self.theme)

    def square(self,picker):
        
        #stopping comparisons being over 12
        x = int(self.theme[0][3])
        if x+3 >12:
            y = x-3
            z = x-6
            a = x-9
        elif x+6 >12:
            y = x+3
            z = x-6
            a = x-9
        elif x+9 >12:
            y = x+3
            z = x+6
            a = x-9
        else:
            y = x+3
            z = x+6
            a = x+9

        #add desired possibilities to nList
        for i in range(len(self.cList)):
            if int(self.cList[i][3]) == y or int(self.cList[i][3]) == z or int(self.cList[i][3]) == a:
                self.nList.append(self.cList[i])
                
        #use nList to pick 3 more colours
        self.theme = picker.random()
        return (self.theme)
            
        
    def random(self):
        for i in range(self.colourNum-1):
            n = randint(0,len(self.nList)-1)
            self.theme.append(self.nList[n])
            self.nList.pop(n)
        print(self.theme)
        return(self.theme)

    def onLeftClick(self,x,y):
        side = 100
        newX = (x//100)*100
        newY = 100+((y//100)*100)
        row = ((newY/100) -4)*-1
        column = (newX/100) +4
        index = int(column + (row*8))
        n = randint(0,len(self.nList)-1)
        self.theme[index] = self.nList[n]
        self.nList.pop(n)

        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.goto(newX,newY)
        t.pendown()
        t.begin_fill()
        t.color(self.theme[index][1])
        for x in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(newX+5,(newY-50))
        t.color("black")
        t.pendown()
        t.write(f"""{self.theme[index][0]}
{self.theme[index][1]}
{self.theme[index][2]}""",True,align="left")
        print(self.theme)

start()
