#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#  A SIMPLE PYTHON SCRIPT FILE FOR CREATING AND READING BLOWFISH ENCRYPTED STRINGS
#              BY TERENCE BROADBENT BSc CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import base64
from Crypto.Cipher import Blowfish

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print "  __   _  _        __  ____  _     _____        _______ ___ ____  _   _    _____ _   _  ____ ___  ____  _____ ____   " 
print " / /_ | || |      / / | __ )| |   / _ \ \      / /  ___|_ _/ ___|| | | |  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "| '_ \| || |_    / /  |  _ \| |  | | | \ \ /\ / /| |_   | |\___ \| |_| |  |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| (_) |__   _|  / /   | |_) | |__| |_| |\ V  V / |  _|  | | ___) |  _  |  | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print " \___/   |_|   /_/    |____/|_____\___/  \_/\_/  |_|   |___|____/|_| |_|  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                                                    "
print "                              BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                               \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

plainText = "Blessent mon coeur d'une langueur monotone."
uniqueKey = 'EnterpriseKey'					# min 4 | max 56 bytes

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display program data to the screen.
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text  : " + plainText
print "Unique Key  : " + uniqueKey

bytes = 8								# 8 bytes length
while len(plainText) % bytes:
   plainText = plainText + "="         		  # Add appropriate padding to plainText

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Encrypt coded message - Base64/Blowfish.
# Modified: N/A
# -------------------------------------------------------------------------------------

cipher = Blowfish.new(uniqueKey)
encrypted = base64.b64encode(cipher.encrypt(plainText))
print "Encrypted   : " + encrypted

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Decrypt coded message - Base64/Blowfish.
# Modified: N/A
# -------------------------------------------------------------------------------------

encrypted = base64.b64decode(encrypted)
print "Decrypted   : " + cipher.decrypt(encrypted).rstrip("=") + "\n"


