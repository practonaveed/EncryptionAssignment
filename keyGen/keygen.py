import sys

def generate_RSA(bits=2048):
    from  Crypto.PublicKey import RSA 
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

    
if __name__ == '__main__':
    def create_file(key,fileName):
        fp = open(fileName,'w')
        fp.write(key)
        fp.close()
        
    pr_K,pu_K = generate_RSA();
    create_file(pr_K,'../reciever/privateKey.txt')
    create_file(pu_K,'../sender/publicKey.txt')
