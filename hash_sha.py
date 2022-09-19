import os 
import hashlib

liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

chaine=str()

 #open text file
text_file = open("hash_sha.txt","w")

for l in liste:
    chaine=l  
    
    for l2 in liste:
        chaine=l+l2
        
        for l3 in liste:
            chaine=l+l2+l3
            
            for l4 in liste:
                chaine=l+l2+l3+l4
        
  
                
        hashed_string= hashlib.sha256(chaine.encode('utf-8')).hexdigest()


        #write string to file
        text_file.write(hashed_string)

#close file
text_file.close()
