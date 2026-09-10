# Self-Verification

## DecodeLabs Project 2: Basic Encryption and Decryption

I checked my project against the requirements before submission.

### Requirements

- [x] Implemented the IPO cycle.
- [x] Created an encryption function.
- [x] Created a decryption function.
- [x] Used `ord()` to work with character values.
- [x] Used `chr()` to convert values back to characters.
- [x] Used `% 26` to keep letters within the alphabet.
- [x] Used a shift key for encryption and decryption.
- [x] Used `(x + n) % 26` for encryption.
- [x] Used `(x - n) % 26` for decryption.
- [x] Preserved spaces and punctuation.
- [x] Tested uppercase and lowercase letters.
- [x] Tested different messages and shift keys.
- [x] Confirmed that decryption returns the original message.
- [x] Added a validation test which returned PASS.
- [x] Explained why Caesar Cipher is not suitable for real-world secure encryption.

## Test Results

### Test 1
Original message: `HELLO WORLD`

Shift key: `3`

Encrypted message: `KHOOR ZRUOG`

Decrypted message: `HELLO WORLD`

### Test 2
Original message: `Hello World!`

Shift key: `3`

Encrypted message: `Khoor Zruog!`

Decrypted message: `Hello World!`

### Test 3
Original message: `DecodeLabs Cybersecurity!`

Shift key: `13`

The message was successfully encrypted and decrypted back to the original message.

Validation result: **PASS**

## Final Check

The program runs successfully and the decrypted messages match the original messages.
