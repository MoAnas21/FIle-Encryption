import random
from Crypto.Cipher import AES
import sys




KeyFile = "Key.txt"
DataFile = "Data.txt"
EncryptedFile = "Encrypted.txt"


# Check for the proper input format
if len(sys.argv)==1:
    pass

elif len(sys.argv)==2:
    DataFile = str(sys.argv[1])
    
elif len(sys.argv)==3:
    DataFile = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
        
elif len(sys.argv) == 4:
    DataFile = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
    EncryptedFile = str(sys.argv[3])
        
else:
    sys.stdout.write("Error : The correct format is python Encryption.py OPTIONAL( Data.txt , Key.txt , Encrypted.txt )\n")
    sys.exit(1)






def Generate_Key():         #generate random key(if needed)
    
    key = b"".join(random.randint(0, 0xFF).to_bytes(1,'big') for i in range(16))
   
    save_key = open(KeyFile, 'wb')
    save_key.write(key)
    save_key.close()
    
    





def Encrypt():              #Encrypt using the key in file key.txt
    
    #get key from file
    get_key = open(KeyFile, 'rb')
    key=get_key.read(16)
    get_key.close()
    
    
    
    #initialisation vector for aes-cbc mode of encryption
    iv = b"".join(random.randint(0, 0xFF).to_bytes(1,'big') for i in range(16))
    
    #initialisation vector is written at the start in plain text
    fout = open(EncryptedFile, 'wb')
    fout.write(iv)
    fout.close()
    
    
    
    fin = open(DataFile, 'r')
    
    
    fout = open(EncryptedFile, 'ab')
    
    #encryption
    aes = AES.new(key, AES.MODE_CBC, iv)
    while True:
        data = fin.read(16)
        n = len(data)
        data_byte = data.encode()
        if n == 0:
            break
        elif n % 16 != 0:
            data_byte += b'\00' * (16 - n % 16)
        encrypted_data = aes.encrypt(data_byte)
        fout.write(encrypted_data)
    fout.close()
    
    


    

if __name__ == "__main__":
    Generate_Key()
    Encrypt()
    