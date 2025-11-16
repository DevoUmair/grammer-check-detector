import string
import time

def simple_brute_force(ciphertext):
    """
    Simple brute-force attack on Caesar Cipher
    """
    alphabet = string.ascii_uppercase
    n = len(alphabet)
    
    print("Ciphertext:", ciphertext)
    print("\nBrute-forcing all possible keys...\n")
    
    start_time = time.time()
    
    for key in range(1, 26):
        plaintext = ''
        for char in ciphertext:
            if char.upper() in alphabet:
                index = alphabet.index(char.upper())
                new_index = (index - key) % n
                if char.isupper():
                    plaintext += alphabet[new_index]
                else:
                    plaintext += alphabet[new_index].lower()
            else:
                plaintext += char
        
        print(f"Key {key:2d}: {plaintext}")
    
    end_time = time.time()
    print(f"\nTime taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    messages = [
        "WKH HDVLHVW FLSKHU WR EUHDN LV WKH FDHVDU FLSKHU!",
        "XJU JTU B QBSUJDMBS CSPVUF GPSDF BUUBDL!",
        "FRUHVSBWLRQ LV WKH SURFHVV"
    ]
    
    for i, ciphertext in enumerate(messages, 1):
        print(f"\n{'='*40}")
        print(f"ATTEMPT {i}")
        print(f"{'='*40}")
        simple_brute_force(ciphertext)