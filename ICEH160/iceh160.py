from time import sleep
import secp256k1 as ice
import re
import random, codecs, time, sys
from tqdm import tqdm
from rich import print

HUNT4BITCOIN = '''[red]
 ▄▄   ▄▄ ▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ 
█  █ █  █    █   █   █  ▄    █
█  █▄█  ██   █   █▄▄▄█ █ █   █
█       ██   █    ▄  █ █ █   █
█   ▄   ██   █   █ █ █ █▄█   █
█  █ █  ██   █   █▄█ █       █
█▄▄█ █▄▄██▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█

    HASH160 ICELANDS LIB  
      ___            ___  
     (o o)          (o o) 
    (  V  ) MIZOGG (  V  )
    --m-m------------m-m--
                   
[/red]'''

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

print(HUNT4BITCOIN)
print('[yellow]\n------------------------------------------------------------------------------[/yellow]')
delay_print(' Good Luck and Happy Hunting HASH160 ICELANDS LIB...')
print('[yellow]\n------------------------------------------------------------------------------[/yellow]')

def save_data():
    with open("winner.txt", "a") as f:
        f.write(f"""\nMatch Found
        Privatekey (dec):  {ran}""")

ice.Load_data_to_memory("btc_sorted.bin", False)

j=0
pbar=tqdm(initial=j) 

prompt= '''
    ************************************
    *                                  *
    *    Option 1.RANDOM      =  1     *
    *    Option 2.SEQUENCE    =  2     *
    ************************************'''

prompt123= '''
    ********************************
    *                              *
    *     Option.1   bits  =1      *
    *     Option.2   bytes =2      *
    ********************************
Type You Choice Here Enter 1-2 :
'''

start=int(input(prompt))
if start == 1:
    promptstart=int(input(prompt123))
    if promptstart == 1:
        x=int(input("start range bits Min 1-255 ->  "))
        y=int(input("stop range bits Max 256 -> "))
        startscan=2**x
        stopscan=2**y
        
    if promptstart == 2:    
        startscan=int(input("start range Min bytes 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
        stopscan=int(input("stop range Max bytes 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
    while True:
        ran = random.randrange(startscan,stopscan)
        c_rmd = ice.privatekey_to_h160(0, True, ran)
        u_rmd = ice.privatekey_to_h160(0, False, ran)
        if ice.check_collision(c_rmd) or ice.check_collision(u_rmd):
            print(ran)
            save_data()
        pbar.update(12)
    
if start == 2:
    promptstart=int(input(prompt123))
    if promptstart == 1:
        x=int(input("start range bits Min 1-255 ->  "))
        y=int(input("stop range bits Max 256 -> "))
        startscan=2**x
        stopscan=2**y
    if promptstart == 2:    
        startscan=int(input("start range Min bytes 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
        stopscan=int(input("stop range Max bytes 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))    
        
    for ran in range(startscan,stopscan):
        c_rmd = ice.privatekey_to_h160(0, True, ran)
        u_rmd = ice.privatekey_to_h160(0, False, ran)
        if ice.check_collision(c_rmd) or ice.check_collision(u_rmd):
            print(ran)
            save_data()
        pbar.update(12)