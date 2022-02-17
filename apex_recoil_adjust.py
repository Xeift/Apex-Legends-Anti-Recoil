import pyautogui
import time
import win32api
import random
import keyboard

horizontal_range = 2
#min_vertical = 3
#max_vertical = 5
min_firerate = 0.03
max_firerate = 0.04
toggle_button = 'caps lock'
enabled = False

def is_mouse_down():    
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

print("Anti-recoil script started!")
if enabled:
    print("ENABLED")
else:
    print("DISABLED")

last_state = False
vertical_o = 0
while True:
    key_down = keyboard.is_pressed(toggle_button)
    for i in range(1,13):
        k = keyboard.is_pressed('f'+str(i))
        if k == True:
            vertical_o = i
            break  
    # print(vertical_o)    
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")
    
    if is_mouse_down() and enabled:
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        #vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const
        vertical_offset = vertical_o
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    time.sleep(0.001)