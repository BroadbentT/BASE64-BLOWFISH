# BASE64/BLOWFISH ENCODER
## A SIMPLE PYTHON SCRIPT FILE TO CREATE AND READ BASE64/BLOWFISH ENCODED TEXT STRINGS USING A CORPORATE ENTERPRISE KEY.

Usage: python base64_blowfish.py

| LANGUAGE | FILENAME           | MD5 HASH                         | CONFIDENTIALITY MODE |
|------    |------              | -------                          | -----                |
| python   | base64_blowfish.py | f7ca18665c89615e6e1c033e278b6312 | CBC                  |

- [x] For more information on 'confidentiality mode' - see https://csrc.nist.gov/Projects/Block-Cipher-Techniques/BCM

### CIPHER BLOCK CHAINING MODE
__The Cipher Block Chaining (CBC) mode__ is a confidentiality mode whose encryption process features the combining (“chaining”) of the plaintext blocks with the previous ciphertext blocks. The CBC mode requires an IV to combine with the first plaintext block.  The IV need not be secret, but it must be unpredictable; the generation of such IVs is discussed in Appendix C. Also, the integrity of the IV should be protected.

### PBKDF2
In cryptology, __Password-Based Key Derivation Function (PBKDF1 and PBKDF2)__ are key derivation functions with a sliding computational cost, used to reduce vulnerabilities to brute force attacks. PBKDF2 is part of RSA Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0, also published as Internet Engineering Task Force's RFC 2898. It supersedes PBKDF1, which could only produce derived keys up to 160 bits long. RFC 8018 (PKCS #5 v2.1), published in 2017, recommends PBKDF2 for password hashing.

### CONSOLE DISPLAY
![Screenshot](picture1.png)

Approved confidentiality modes include:-

> CBC: An IV-based encryption scheme, the mode is secure as a probabilistic encryption scheme, achieving indistinguishability from random bits, assuming a random IV. 
> Confidentiality is not achieved if the IV is merely a nonce, nor if it is a nonce enciphered under the same key used by the scheme, as the standard incorrectly suggests to do. 
> Ciphertexts are highly malleable. 
> No chosen ciphertext attack (CCA) security. 
> Confidentiality is forfeit in the presence of a correct-padding oracle for many padding methods.
> Encryption inefficient from being inherently serial.
> Widely used, the mode’s privacy-only security properties result in frequent misuse.
> Can be used as a building block for CBC-MAC algorithms. I can identify no important advantages over CTR mode.

> CFB: Cipher feedback is an IV-based encryption scheme, the mode is secure as a probabilistic encryption scheme, achieving indistinguishability from random bits, assuming a random IV. 
> However, confidentiality is not achieved if the IV is predictable, nor if it is made by a nonce enciphered under the same key used by the scheme, as the standard incorrectly suggests to do.
> Ciphertexts are malleable. 
> No CCA-security. 
> Encryption inefficient from being inherently serial.
