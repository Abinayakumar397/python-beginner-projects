def encrypt_msg(msg,n):
    
    cipher_value=[]
   
    for j in msg:
            if j==" ":
                 cipher_value+=" "
            else:
              value=letters[j]
              encryption=(value+n)%26
              cipher_value.append(encryption)
        
    cipher_text=""
    for k in cipher_value:
        if k==" ":
            cipher_text+=" "
        else:
         letter=letters_reverse[k]
         cipher_text+=letter
    return cipher_text

def decrypt_msg(ct,n):
    plain_index=[]   
    for k in ct:
        if k==" ":
            plain_index+=" "
        else:
            value=letters[k]
            decryption=(value-n)%26
            
            plain_index.append(decryption)
    plain_text=""
    for j in plain_index:
        if j==" ":
            plain_text+=" "
        else:
           letter=letters_reverse[j]
           plain_text+=letter
    return plain_text


letters={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
letters_reverse={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}


type=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")
if type=='encrypt':
   message=input("Type your message:")
   shift=int(input("Type your shift number:"))
   cipher_text=encrypt_msg(message,shift)
   print("Here's the encrypted result:"+cipher_text)
  
else:
    message =input("Type your message:")
    shift=int(input("Type the shift number:"))
    plain_text=decrypt_msg(message,shift)
    print("Here's the decrypt result:",plain_text)
  

