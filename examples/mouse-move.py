# This script demonstrates how to move the mouse cursor using the pyautogui library.
import pyautogui as pag

# Move the mouse to a specific location
pag.moveTo(960, 540, duration=1)  # Adjust coordinates based on your screen resolution

# Move the mouse in a circular path
for i in range(360):            
    x = 960 + 100 * pag.cos(pag.radians(i))  # Circle radius of 100 pixels
    y = 540 + 100 * pag.sin(pag.radians(i))
    pag.moveTo(x, y, duration=0.01)  # Move to the calculated position
