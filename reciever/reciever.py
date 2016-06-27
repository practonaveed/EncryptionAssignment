# Here Sender uses the public key of the reciever to encrypt the AES Key
# AES here is used to encrypt the message
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import  base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def aesDecrypt( key, enc ):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return unpad(cipher.decrypt( enc[16:] ))
    
def rsaDecrypt(keyObj,enc):
    msg = keyObj.decrypt(enc)
    return msg
    
def file2String(fileName):
    fp = open(fileName)
    return ''.join(fp.readlines())
    
def rsaKeyImport(fileName="privateKey.txt"):
    key = file2String(fileName)
    return RSA.importKey(key)
    
def messageRetrieve(fileName):
    return file2String(fileName)
    
def write2file(string,fileName):
    fp = open(fileName,'w')
    fp.write(string)
    
if __name__ == "__main__":
    keyCipher = messageRetrieve("../senderOp/keyCipher.txt")
    msgCipher = messageRetrieve("../senderOp/msgCipher.txt")
    privateKey = rsaKeyImport()
    aesKey = rsaDecrypt(privateKey,keyCipher)
    msg = aesDecrypt(aesKey,msgCipher)
    write2file(msg,'../recieverOp/msg.txt')