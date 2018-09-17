import argparse
import sys
import time
import sys
import subprocess
import os

def main():
    print("""
______               _         ______  _        
| ___ \             | |        | ___ \(_)       
| |_/ / _ __  _   _ | |_   ___ | |_/ / _  _ __  
| ___ \| '__|| | | || __| / _ \| ___ \| || '_ \ 
| |_/ /| |   | |_| || |_ |  __/| |_/ /| || | | |
\____/ |_|    \__,_| \__| \___|\____/ |_||_| |_|

          ==> Developed by e4x  <== 
    ==> brute-force tool for executables <==
    \--------------------------------------/
                 BruteBin v1

    	""")
main()


parser = argparse.ArgumentParser(description="Manual")
parser.add_argument("--file",dest="FILE",action="store",required=False,help="File to brute")
parser.add_argument("--list",dest="LIST",action="store",required=False,help="Your wordlist")
parser.add_argument("--error",dest="ERROR",action="store",required=False,help="Error message")
arguments = parser.parse_args()

def brute():
    print("[*] Opening the wordlist ...")
    time.sleep(1)
    wd = open(arguments.LIST,"r")
    print("[*] Starting sequence ...\n")
    for x in wd:
        output = str(subprocess.Popen("./"+arguments.FILE + '\t'+x,shell=True,stdout=subprocess.PIPE).stdout.read())
        if(arguments.ERROR in output):
            time.sleep(1)
            print("[+] Sequence: {}[-] Error found\n".format(x))
            continue
        else:
            time.sleep(1)
            print("\n[+] Sequence: {}[+] Error not found\n".format(x))
            break
brute()