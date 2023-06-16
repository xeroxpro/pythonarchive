import os

def ayristir(path):
    dirList=os.listdir(path)
    dirList.sort()

    fnames = []
    dnames = []

    for fname in dirList:
        if os.path.isdir(path + fname):
            dnames.append(fname)
        if os.path.isfile(path + fname):
            fnames.append(fname)

    return dnames,fnames

(klasorler,dosyalar) = ayristir("\\TEGVFILER\_Bilgi_Teknolojileri\Aylik_Rapor")

for item in klasorler:
    print("Directory => " + item)

for item in dosyalar:
    print("File => " + item)