###############################################################################################################################
#Collaborators: Jordan Edgel, Kaleb Rhody, Thomas Presicci, Alex Reed
#Description: A series of trivia questions asked entirely in Morse Code to be solved by competitors. Players are scored by time.
#Due Date: May 10, 2017
###############################################################################################################################
from time import *
import pygame
import RPi.GPIO as GPIO
from Tkinter import *


class Game(Canvas):
        def __init__(self, master):
                self.master = master
                Canvas.__init__(self,master)
                master.columnconfigure(0, weight = 1)
                master.rowconfigure(0, weight = 1)
                
        def gui(self):
                self.grid()
                
                img = PhotoImage( file = "neil.gif" )
                self.pic = Label(self.master, image = img, height = 40, width = 40)
                self.pic.image = img
                self.pic.grid(row = 0, column = 0, sticky = N+S+E+W)

                self.ansA = Radiobutton(self.master, text = atext, value = 1, variable = ansvar, width = 10)
                self.ansA.grid(row = 1, column = 0)
                self.ansB = Radiobutton(self.master, text = btext, value = 2, variable = ansvar, width = 10)
                self.ansB.grid(row = 2, column = 0)
                self.ansC = Radiobutton(self.master, text = ctext, value = 3, variable = ansvar, width = 10)
                self.ansC.grid(row = 1, column = 1)
                self.ansD = Radiobutton(self.master, text = dtext, value = 4, variable = ansvar, width = 10)
                self.ansD.grid(row = 2, column = 1)

                self.timer = Label(self.master, text = "Time: ", state = DISABLED, height = 5, width = 25)
                self.timer.grid(row = 0, column = 2, columnspan = 2, sticky = W)

                self.qNumber = Label(self.master, text = "Question #", state = DISABLED, height = 5, width = 25)
                self.qNumber.grid(row = 1, column = 2, columnspan = 2, sticky = N+W)

                self.submit = Button(self.master, text = testvar, height = 2, width = 10, command = self.checkAns)
                self.submit.grid(row = 3, column = 2, columnspan = 2)

        def play(self):
                self.gui()
        
        def morsestuff(self):
                pass

        def ledstuff(self):
                pass

        def timerstuff(self):
                pass
        
        def checkAns(self):
            if(ansvar.get() == 1):
                testvar = "ans 1"
            elif(ansvar.get() == 2):
                testvar = "Ans 2"
            elif(ansvar.get() == 3):
                testvar = "Ans 3"
            elif(ansvar.get() == 4):
                testvar = "Ans 4"
            print testvar
        
        def score(self):
                i = 0
                timer.append(i)
                while running == True:
                        timer.remove(i)
                        sleep(1)
                        i += 1
                        timer.append(i)
                        print timer
                
               
                                
        def penalize(self):
                pass
                

atext = "placeholder a"
btext = "placeholder b"
ctext = "placeholder c"
dtext = "placeholder d"
testvar = ""
window = Tk()
ansvar = IntVar()

penalty = 0
running = True
score = score()
timer = []

questdict = {1:3, 2:2, 3:4, 4:1}
question1 = []
question2 = []
question3 = []
question4 = []

window.title("Space with Tyson")
window.geometry("500x400")
f = Game(window)
f.play()
window.mainloop()

