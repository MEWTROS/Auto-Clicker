import time
import pyautogui
import keyboard 
from pynput.keyboard import Listener
import threading
a=False
b=None
autol=None
autotype=None
speed=None
def  getdata():
    global autol
    global autotype
    global speed
    autotype=input("Do you wish to auto-click a keyboard or a mouse button (K/M) :")
    if autotype=='K' or autotype=='k':
      autol=input("Enter the key to be autoclicked :")
      speed=int(input("Enter the speed of autoclicking :"))
      print("press UP key to turn ON \npress DOWN key to turn OFF\n")
    elif autotype=='M' or autotype=='m':
      autol=input("Enter the mouse button (RIGHT/LEFT) :")
      autol=autol.lower()
      speed=int(input("Enter the speed of autoclicking :"))
      print("press UP key to turn ON \npress DOWN key to turn OFF\n")
     
getdata()
def autoclick():
    global autol
    global a
    global autotype
    global speed
    while a:
        if autotype=='K' or autotype=='k':
            pyautogui.press(autol,presses=speed)
        elif autotype=='M' or autotype=='m':
            pyautogui.click(button=autol,clicks=speed)
        

    
def write_to_file(key):
    global a,b
    letter = str(key)
    letter = letter.replace("'", "")


    if letter == 'Key.up':
        print("AUTO CLICKER ON")
        a=True
        print("STARTING IN 10 SECONDS")
        time.sleep(10)
        if b is None or not b.is_alive():
            b = threading.Thread(target=autoclick)
            b.start()
    elif letter == 'Key.down':
        print("AUTO CLICKER OFF\n")
        a=False
        autoclick()
with Listener(on_press=write_to_file) as l:
    l.join()
        

# def autoclickmouse():
#     global autol
#     while a:
#         pyautogui.click(button=autol,clicks=5)
        
        
# def to_file(key):
#     global a,b
#     letter = str(key)
#     letter = letter.replace("'", "")


#     if letter == 'Key.up':
#         print("AUTO CLICKER ON")
#         a=True
#         print("STARTING IN 10 SECONDS")
#         time.sleep(10)
#         if b is None or not b.is_alive():
#             b = threading.Thread(target=autoclickmouse)
#             b.start()
#     elif letter == 'Key.down':
#         print("AUTO CLICKER OFF")
#         a=False
#         autoclickmouse()

# with Listener(on_press=to_file) as l:
#     l.join()

    
   


     