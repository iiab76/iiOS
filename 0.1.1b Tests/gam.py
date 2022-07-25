import time
import psutil
import os

battery = psutil.sensors_battery()

print("""
╔╦╦═╦══╗
╠╬╣║║══╣
║║║║╠══║
╚╩╩═╩══╝
""")

print("""
░██████╗░░█████╗░███╗░░░███╗███████╗███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")
print("Welcome to the GAMEMASTER!")
print(" ")
print("==================================================")
print(" ")
print(time.strftime("%m/%d/%y"))
print("--------------------------------------------------")
print("Battery level: ")
print(battery.percent)
print("--------------------------------------------------")
print("""
[1] Snake
[2] Minecraft by Cyber Coding - Not available to play
[3] Pong - Not available to play
[4] Battleships
""")
game = input("||>>: ")
if game == '1':
    os.startfile('sna.py')
if game == '2':
    os.startfile('')
if game == '3':
    os.startfile('pong.py')
if game == '4':
    os.startfile('bat.py')
input()