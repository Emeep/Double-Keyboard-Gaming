import win32api, win32con
import time

sensitivity = 30

aiming = False
shooting = False

while True:
    a = win32api.GetKeyState(0x26)  # up arrow key
    if a < 0:
        break

while True:
    up = win32api.GetKeyState(0x50) # P
    left = win32api.GetKeyState(0x4C) # L
    down = win32api.GetKeyState(0xBA) # ;
    right = win32api.GetKeyState(0xDE) # '
    
    aim = win32api.GetKeyState(0xDC) # \
    shoot = win32api.GetKeyState(0x4B) # K

    if up != 0 and up != 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -sensitivity)
    if left != 0 and left != 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -sensitivity, 0)
    if down != 0 and down != 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, sensitivity)
    if right != 0 and right != 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, sensitivity, 0)
    
    if aim != 0 and aim != 1 and not aiming:
        aiming = True
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.016)
    elif aim == 0 or aim == 1 and aiming:
        aiming = False
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    if shoot != 0 and shoot != 1 and not shooting:
        shooting = True
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.016)
    elif shoot == 0 or shoot == 1 and shooting:
        shooting = False
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    time.sleep(0.016)
