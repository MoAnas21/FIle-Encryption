import numpy as np
import cv2
import sys
import random
from Crypto.Cipher import AES




KeyFile = "Key.txt"
Data_Image = "image.jpg"
Encrypted_Image = "Encrypted_Image.png"

# Check for the proper input format
if len(sys.argv) == 1 :
    pass

elif len(sys.argv)==2:
    Data_Image = str(sys.argv[1])
    
elif len(sys.argv)==3:
    Data_Image = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
       
elif len(sys.argv) == 4:
    Data_Image = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
    Encrypted_Image = str(sys.argv[3])
        
else:
    sys.stdout.write("Error : The correct format is python Encryption.py OPTIONAL( DataImage.jpg , Key.txt , EncryptedImage.png )\n")
    sys.exit(1)






def Generate_Key():         #generate random key and initialisation vector(if needed)
    
    key = b"".join(random.randint(0, 0xFF).to_bytes(1,'big') for i in range(16))
    iv = b"".join(random.randint(0, 0xFF).to_bytes(1,'big') for i in range(16))
   
    save_key = open(KeyFile, 'wb')
    save_key.write(key)
    save_key.write(iv)
    save_key.close()






def Encrypt():              #Encrypt using the key and iv in file key.txt
    
    #Get the Key
    get_key = open(KeyFile, 'rb')
    key = get_key.read(16)
    iv = get_key.read(16)
    get_key.close()
    
    
    #Read the Image Data and split to matrices of red green blue
    data_image = cv2.imread(Data_Image,1)  
    (r,c,n) = data_image.shape
    red, green, blue = cv2.split(data_image)
    
    
    #Create an encrypted data matrix
    encrypted_image = np.ndarray((r,c,3),dtype='uint8')
    
    
    #Split matrix to byte array 
    array_r = bytearray(red)
    encrypted_array_r = array_r
    array_g = bytearray(green)
    encrypted_array_g = array_g
    array_b = bytearray(blue)
    encrypted_array_b = array_b
    
    
    #Encrypt
    aes = AES.new(key, AES.MODE_CBC, iv)
    i=0;
    while True:
        data_r = array_r[i:i+16]
        data_g = array_g[i:i+16]
        data_b = array_b[i:i+16]
        n = len(data_r)
        if n == 0:
            break
        elif n % 16 != 0:
            data_r += b'\00' * (16 - n % 16)
            data_g += b'\00' * (16 - n % 16)
            data_b += b'\00' * (16 - n % 16)
        encrypted_array_r [i:i+16] = aes.encrypt(data_r)
        encrypted_array_g [i:i+16] = aes.encrypt(data_g)
        encrypted_array_b [i:i+16] = aes.encrypt(data_b)
        i = i+16
        
    
    #Fill the encrypted data matrix
    for i in range(r):
        for j in range(c):
            encrypted_image[i][j][0] = np.uint8(encrypted_array_r[i*c+j])
            encrypted_image[i][j][1] = np.uint8(encrypted_array_g[i*c+j])
            encrypted_image[i][j][2] = np.uint8(encrypted_array_b[i*c+j])
        
        
    #Write to an image file
    cv2.imwrite(Encrypted_Image, encrypted_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 
   



 
    
if __name__ == "__main__":
    Generate_Key()
    Encrypt()

