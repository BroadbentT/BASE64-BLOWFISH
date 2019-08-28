# BASE64/BLOWFISH ENCODER
## A SIMPLE PYTHON SCRIPT FILE TO CREATE AND READ BASE64/BLOWFISH ENCODED TEXT STRINGS USING A CORPORATE ENTERPRISE KEY.

Usage: python base64_blowfish.py

| LANGUAGE | FILENAME           | MD5 HASH                         | CONFIDENTIALITY MODE |
|------    |------              | -------                          | -----                |
| python   | base64_blowfish.py | f7ca18665c89615e6e1c033e278b6312 | CBC                  |

- [x] For more information on 'confidentiality mode' - see https://csrc.nist.gov/Projects/Block-Cipher-Techniques/BCM

### PBKDF2
In cryptology, __Password-Based Key Derivation Function (PBKDF1 and PBKDF2)__ are key derivation functions with a sliding computational cost, used to reduce vulnerabilities to brute force attacks. PBKDF2 is part of RSA Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0, also published as Internet Engineering Task Force's RFC 2898. It supersedes PBKDF1, which could only produce derived keys up to 160 bits long. RFC 8018 (PKCS #5 v2.1), published in 2017, recommends PBKDF2 for password hashing.

### CIPHER BLOCK CHAINING MODE
__The Cipher Block Chaining (CBC) mode__ is a confidentiality mode whose encryption process features the combining (“chaining”) of the plaintext blocks with the previous ciphertext blocks. The CBC mode requires an IV to combine with the first plaintext block.  The IV need not be secret, but it must be unpredictable; the generation of such IVs is discussed in Appendix C. Also, the integrity of the IV should be protected.

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
> Scheme depends on a parameter s, 1 ≤ s ≤ n, typically s = 1 or s = 8. Inefficient for needing one blockcipher call to process only s bits. 
> The mode achieves an interesting  “self-synchronization” property; insertion or deletion of any number of s-bit characters into the ciphertext only temporarily disrupts correct decryption.

> CTR: An IV-based encryption scheme, the mode achieves indistinguishability from random bits assuming a nonce IV.
> As a secure nonce-based scheme, the mode can also be used as a probabilistic encryption scheme, with a random IV.
> Complete failure of privacy if a nonce gets reused on encryption or decryption.
> The parallelizability of the mode often makes it faster, in some settings much faster, than other confidentiality modes.
> An important building block for authenticated-encryption schemes.
> Overall, usually the best and most modern way to achieve privacy-only encryption.

> ECB: A blockcipher, the mode enciphers messages that are a multiple of n bits by separately enciphering each n-bit piece.
> The security properties are weak, the method leaking equality of blocks across both block positions and time. 
> Of considerable legacy value, and of value as a building block for other schemes, but the mode does not achieve any generally desirable security goal in its own right and must be used with considerable caution; ECB should not be regarded as a “general-purpose” confidentiality mode.

> OFB: An IV-based encryption scheme, the mode is secure as a probabilistic encryption scheme, achieving indistinguishability from random bits, assuming a random IV. 
> Confidentiality is not achieved if the IV is a nonce, although a fixed sequence of IVs (eg, a counter) does work fine. 
> Ciphertexts are highly malleable.
> No CCA security.
> Encryption and decryption inefficient from being inherently serial.
> Natively encrypts strings of any bit length (no padding needed). 
> I can identify no important advantages over CTR mode.

> XTS: An IV-based encryption scheme, the mode works by applying a tweakable blockcipher (secure as a strong-PRP) to each n-bit chunk.
> For messages with lengths not divisible by n, the last two blocks are treated specially. 
> The only allowed use of the mode is for encrypting data on a block-structured storage device. 
> The narrow width of the underlying PRP and the poor treatment of fractional final blocks are problems. 
> More efficient but less desirable than a (wide-block) PRP-secure blockcipher would be.

More information is available here - https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf


