import time
from time import sleep
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import messagebox

RPi.GPIO.setmode(RPi.GPIO.BOARD)   

led = LED(14)    

win = Tk()    
win.title("Morse Code")    
Font = tkinter.font.Font(family = 'Cambria' , size = 14, weight = "bold")

morse_code = {
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

def dot():
    led.on()
    time.sleep(0.02)
    led.off
    
def dash():
    led.on()
    time.sleep(1.8)
    led.off()
    
def gap():
    led.off()
    time.sleep(2)

def morseToString(Name):
    morse_string = ""
    if len(Name) > 0 and len(Name) <= 12:
        for c in Name:
            morse_string += morse_code[c.upper()]
            morse_string += " "
        return morse_string
    else:
        messagebox.showerror("Error", "Name cannot exceed 12 characters or null")
        return ""

def Sentence():
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

def close():
    led.off()
    win.destroy()

Name = Entry(win,font=Font, width=30) 
Name.grid(row=0, column=1)

launch = Button(win,text='SUBMIT', font=Font, command= Sentence,bg='green', height=1, width=13)
launch.grid(row=1, column=1)

exitButton = Button(win, text = 'Exit', font  = Font, command = close, bg = 'red', width = 14) 
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
