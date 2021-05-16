import numpy as np
import cv2
import sys
from Crypto.Cipher import AES




KeyFile = "Key.txt"
Encrypted_Image = 'Encrypted_Image.png'
Decrypted_Image = 'Decrypted_image.jpg'

# Check for the proper input format
if len(sys.argv) == 1 :
    pass

elif len(sys.argv)==2:
    Encrypted_Image = str(sys.argv[1])
    
elif len(sys.argv)==3:
    Encrypted_Image = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
        
elif len(sys.argv) == 4:
    Encrypted_Image = str(sys.argv[1])
    KeyFile = str(sys.argv[2])
    Decrypted_Image = str(sys.argv[3])
        
else:
    sys.stdout.write("Error : The correct format is python Decryption.py OPTIONAL( EncryptedImage.png , Key.txt , DecryptedImage.jpg )\n")
    sys.exit(1)






def Decrypt():              #Decrypt using the key and iv in file key.txt
    


    #Get the Key
    get_key = open(KeyFile, 'rb')
    key = get_key.read(16)
    iv = get_key.read(16)
    get_key.close()
    
    
    #Read the Encrypted Image Data and split to matrices of red green blue
    data_image = cv2.imread(Encrypted_Image,1)  
    (r,c,n) = data_image.shape
    red, green, blue = cv2.split(data_image)
    
    
    #Create a decrypted data matrix
    decrypted_image = np.ndarray((r,c,3),dtype='uint8')
    
    
    #Split matrix to byte array 
    array_r = bytearray(red)
    decrypted_array_r = array_r
    array_g = bytearray(green)
    decrypted_array_g = array_g
    array_b = bytearray(blue)
    decrypted_array_b = array_b
    
    
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
        decrypted_array_r [i:i+16] = aes.decrypt(data_r)
        decrypted_array_g [i:i+16] = aes.decrypt(data_g)
        decrypted_array_b [i:i+16] = aes.decrypt(data_b)
        i = i+16
        
    
    #Fill the encrypted data matrix
    for i in range(r):
        for j in range(c):
            decrypted_image[i][j][0] = np.uint8(decrypted_array_r[i*c+j])
            decrypted_image[i][j][1] = np.uint8(decrypted_array_g[i*c+j])
            decrypted_image[i][j][2] = np.uint8(decrypted_array_b[i*c+j])
        
        
    #Write to an image file
    cv2.imwrite(Decrypted_Image, decrypted_image) 
    
    


if __name__ == "__main__":
    Decrypt()