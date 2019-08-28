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
from Crypto import Random
from Crypto.Cipher import Blowfish
from Crypto.Protocol.KDF import PBKDF2

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print " ____   __   _  _        __  ____  _     _____        _______ ___ ____  _   _    _____ _   _  ____ ___  ____  _____ ____   " 
print "| __ ) / /_ | || |      / / | __ )| |   / _ \ \      / /  ___|_ _/ ___|| | | |  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  "
print "|  _ \| '_ \| || |_    / /  |  _ \| |  | | | \ \ /\ / /| |_   | |\___ \| |_| |  |  _| |  \| | |  | | | | | | |  _| | |_) | "
print "| |_) | (_) |__   _|  / /   | |_) | |__| |_| |\ V  V / |  _|  | | ___) |  _  |  | |___| |\  | |__| |_| | |_| | |___|  _ <  "
print "|____/ \___/   |_|   /_/    |____/|_____\___/  \_/\_/  |_|   |___|____/|_| |_|  |_____|_| \_|\____\___/|____/|_____|_| \_\ "
print "                                                                                                                           "
print "                                  BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                                  \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

plainText  = "Blessent mon coeur d'une langueur monotone"
companyKey = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'

blockSize  = 32 				# 16 to 256 bytes, in multiples of 16 in length.
padding    = lambda s: s + (blockSize - len(s) % blockSize) * chr(blockSize - len(s) % blockSize)
unpad      = lambda s: s[:-ord(s[len(s) - 1:])]

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

def Key(companyKey):
   salt = b'Pots de sel et de poivre'
   key = PBKDF2(companyKey, salt, 64, 1000)
   return key[:32]					# Max key size = 56 bytes.

def encrypt(plainText, companyKey):
   privateKey = Key(companyKey)
   text = padding(plainText)
   blocksize = Blowfish.block_size
   iv = Random.new().read(blocksize)
   cipher = Blowfish.new(privateKey, Blowfish.MODE_CBC, iv)
   return base64.b64encode(iv + cipher.encrypt(text))

def decrypt(encryption, companyKey):
   privateKey = Key(companyKey)
   decrypted = base64.b64decode(encryption)
   iv = decrypted[:8]						# Fixed at 8 bytes.
   cipher = Blowfish.new(privateKey, Blowfish.MODE_CBC, iv)
   return unpad(cipher.decrypt(decrypted[8:]))   		# Fixed at 8 bytes.

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Display program variables, and encrypt/decrypt plainText.
# Modified: N/A
# -------------------------------------------------------------------------------------

print "Plain Text  : " + plainText
print "Company Key : " + companyKey
print "Unique Salt : Pots de sel et de poivre"
print "Private Key : " + base64.b64encode(Key(companyKey))
print "Cipher Mode : CBC\n"

encrypted = encrypt(plainText, companyKey)
print "Encrypted   : " + encrypted
 
decrypted = decrypt(encrypted, companyKey)
print "Decrypted   : " + decrypted + "\n"
