import random
from time import sleep
from win32api import *
from win32con import *

print('[ANTI-AFK] : Switch to the Minecraft window.')
print()

print()

print('Script starting in 5...')
sleep(1)
print('4...')
sleep(1)
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)

print()

print('Started!')

print()

sleep_time = random.randrange(10, 25)

while True:

    keybd_event(VK_SPACE, 0,0,0)
    sleep(.05)
    keybd_event(VK_SPACE, 0,KEYEVENTF_KEYUP,0)
    print('Spacebar Pressed.')
    
    sleep(sleep_time)
