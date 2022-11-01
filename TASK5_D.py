# Libraries used for the task -

import time          
from time import sleep
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import messagebox

RPi.GPIO.setmode(RPi.GPIO.BOARD)   # using the GPIO Board setup for the task

led = LED(14)    # I am using GPIO pin 14, i-e physical pin 8

win = Tk()    # creating a gui titled "Morse Code"
win.title("Morse Code")    
Font = tkinter.font.Font(family = 'Cambria' , size = 14, weight = "bold") # Here I have selected the font and size 

morse_code = {      # Here I have defined every character in morse code 
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
}

def dot():   # I have defined the dot function for my code-
    led.on()
    time.sleep(0.02)
    led.off
    
def dash():  # I have defined the dash function for my code -
    led.on()
    time.sleep(1.8)
    led.off()
    
def gap():  # Here I have created a gap function for creating a space between 2 letters
    led.off()
    time.sleep(2)

def morseToString(Name): # Here I have created a function that takes the input and compares it with our letter dictionary  
    morse_string = ""
    if len(Name) > 0 and len(Name) <= 12: # here I fixed the lenght of the string input
        for c in Name:
            morse_string += morse_code[c.upper()]
            morse_string += " "
        return morse_string
    else:
        messagebox.showerror("Error", "Name cannot exceed 12 characters or null") # Then the input string doesn't fits the fixed lenght this message would be displayed
        return ""

def Sentence(): # This function fetches the converted string and compares it with the letter dictionary and then prints the sentence in morse code
    led.off()
    senText = Name.get()
    conversion = morseToString(senText)
    print(conversion)
    for inp in conversion:
          for letter in inp:
              if letter == ".":
                 dot()
                 time.sleep(0.3)
              elif letter == "-":
                 dash()
                 time.sleep(1)
              elif letter == " ":
                 gap()
                 led.off()

led.off()

def close(): # Exit command
    led.off()
    win.destroy()

 # Creations of the buttons - 

Name = Entry(win,font=Font, width=30) 
Name.grid(row=0, column=1)

launch = Button(win,text='SUBMIT', font=Font, command= Sentence,bg='green', height=1, width=13)
launch.grid(row=1, column=1)

exitButton = Button(win, text = 'Exit', font  = Font, command = close, bg = 'red', width = 14) 
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
