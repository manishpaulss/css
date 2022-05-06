class CaesarCipher:
    
    def __init__(self, n:int = 5):
        self.n = n
        
    def encrypt(self, message:str):
        encrypted_message = ""
        for x in message:
            if not x.isalpha():
                encrypted_message += x;
                continue;
            if x.isupper():
                encrypted_message += chr(((ord(x) + self.n - 65) % 26) + 65)
            else:
                encrypted_message += chr(((ord(x) + self.n - 97) % 26) + 97)

        return encrypted_message
    
    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for x in encrypted_message:
            if not x.isalpha():
                decrypted_message += x;
                continue;
            sub = None
            if x.isupper():
                sub = 65
            else:
                sub = 97
            
            val = ((ord(x) - self.n - sub) % 26)
            if val >= 0:
                decrypted_message += chr(val + sub)
            else:
                decrypted_message += chr(val + sub + 26)
            
        return decrypted_message


message = input("Message to encrypt: ")
n = int(input("Key: "))

cc = CaesarCipher(n)
cipher = cc.encrypt(message)
decrypt = cc.decrypt(cipher)
print(f"Encrypted message: {cipher}")
print(f"Decrypted message: {decrypt}")