# Here Sender uses the public key of the reciever to encrypt the AES Key
# AES here is used to encrypt the message
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import  base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

def aesKeyGenerate():
    aeskey = Random.new().read(32)
    return aeskey
    
def aesEncrypt( key, raw ):
    raw = pad(raw)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( raw ) ) 
    
def rsaEncrypt(message,keyObj):
    #cipher = PKCS1_OAEP.new(key)
    ciphertext = keyObj.encrypt(message,'x')[0]
    return ciphertext
    
def file2String(fileName):
    fp = open(fileName)
    return ''.join(fp.readlines())
    
def rsaKeyImport(fileName="publicKey.txt"):
    key = file2String(fileName)
    return RSA.importKey(key)
    
def messageRetrieve(fileName="message.txt"):
    return file2String(fileName)
    
def write2file(string,fileName):
    fp = open('../senderOp/'+fileName,'w')
    fp.write(string)
    
if __name__ == "__main__":
    aesKey = aesKeyGenerate()
    message = messageRetrieve()
    msgCipher = aesEncrypt(aesKey,message)
    publicKey = rsaKeyImport()
    keyCipher = rsaEncrypt(aesKey,publicKey)
    write2file(msgCipher,'msgCipher.txt')
    write2file(keyCipher,'keyCipher.txt')