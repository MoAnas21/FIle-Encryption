from Crypto.Cipher import AES
import sys




KeyFile = "Key.txt"
EncryptedFile = "Encrypted.txt"
DecryptedFile = "Decrypted.txt"


# Check for the proper input format
if len(sys.argv) == 1 :
    pass

elif len(sys.argv)==2:
    EncryptedFile = str(sys.argv[1])
    
elif len(sys.argv)==3:
    EncryptedFile = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
        
elif len(sys.argv) == 4:
    EncryptedFile = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
    DecryptedFile = str(sys.argv[3])
        
else:
    sys.stdout.write("Error : The correct format is python Encryption.py OPTIONAL( Encrypted.txt , Key.txt , Decrypted.txt )\n")
    sys.exit(1)







def Decrypt():              #Decrypt using the key in file key.txt

    #Get the Key
    get_key = open(KeyFile, 'rb')
    key=get_key.read(16)
    get_key.close()
    
    
    #Decrypt
    fin = open(EncryptedFile, 'rb')
    iv = fin.read(16)
    fin.seek(16,0)
    aes = AES.new(key, AES.MODE_CBC, iv)
    fout = open(DecryptedFile, 'w')
    while True:
        encrypted_data = fin.read(16)
        n = len(encrypted_data)
        if n == 0:
            break
        decrypted_data = aes.decrypt(encrypted_data)
        decoded_data = decrypted_data.decode()
        fout.write(decoded_data)
    fin.close()
    fout.close()





if __name__ == "__main__":
    Decrypt()
